# CIS 731: Databricks to Docker DevContainer Porting Guide (Distributed ML)

## 1. Updating the DevContainer `Dockerfile`

To run `scikit-learn` pipelines distributed over Spark workers via `joblib`, you must add the data science and bridging libraries to your existing Python environment. 

Update the `RUN pip install` block in your `Dockerfile` to include `pandas`, `scikit-learn`, `xgboost`, `joblib`, and `joblibspark`. Pin the versions to match the ecosystem timing of your existing Spark 3.5 and PyTorch 2.2 dependencies.

```dockerfile
# ==============================================================================
# CIS 531/731: DevContainer Dockerfile (Updated for Distributed ML)
# ==============================================================================
FROM python:3.10-slim-bullseye

# 1. Install System Dependencies (Java for PySpark, FFmpeg for Whisper)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    openjdk-11-jre-headless \
    ffmpeg \
    git \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# 2. Configure Environment Variables
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PYSPARK_PYTHON=python3
ENV PIP_NO_CACHE_DIR=1

# 3. Install Python Dependencies
RUN pip install --upgrade pip && \
    pip install \
    pyspark==3.5.1 \
    torch==2.2.1 \
    transformers==4.38.2 \
    openai-whisper==20231117 \
    mlflow==2.11.1 \
    faiss-cpu==1.8.0 \
    pandas==2.2.1 \
    scikit-learn==1.4.1 \
    xgboost==2.0.3 \
    joblib==1.3.2 \
    joblibspark==0.5.3

# 4. Create Non-Root User
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID$USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m$USERNAME -s /bin/bash \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME
WORKDIR /workspace
```

## 2. Docker Compose Configuration

To route your workspace to a multi-node Spark cluster and a persistent MLflow server, create a `docker-compose.yml` file in your repository root. This orchestrates your custom DevContainer (`workspace`) alongside the open-source Bitnami Spark images and the MLflow UI.

```yaml
version: '3.8'

services:
  # The DevContainer (Your active development environment)
  workspace:
    build: 
      context: .
      dockerfile: Dockerfile
    container_name: cis731-workspace
    volumes:
      - .:/workspace
    network_mode: bridge
    command: sleep infinity
    depends_on:
      - spark-master
      - mlflow-server

  # Local Spark Master Node
  spark-master:
    image: bitnami/spark:3.5
    container_name: spark-master
    environment:
      - SPARK_MODE=master
    ports:
      - "8080:8080" # Spark Master Web UI
      - "7077:7077" # Spark RPC Port
    volumes:
      - ./data:/opt/bitnami/spark/data

  # Spark Worker 1
  spark-worker-1:
    image: bitnami/spark:3.5
    container_name: spark-worker-1
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark-master:7077
      - SPARK_WORKER_MEMORY=2G
      - SPARK_WORKER_CORES=1
    depends_on:
      - spark-master
    volumes:
      - ./data:/opt/bitnami/spark/data

  # Spark Worker 2
  spark-worker-2:
    image: bitnami/spark:3.5
    container_name: spark-worker-2
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark-master:7077
      - SPARK_WORKER_MEMORY=2G
      - SPARK_WORKER_CORES=1
    depends_on:
      - spark-master
    volumes:
      - ./data:/opt/bitnami/spark/data

  # Local MLflow Tracking Server
  mlflow-server:
    image: ghcr.io/mlflow/mlflow:v2.11.1
    container_name: mlflow-server
    ports:
      - "5000:5000" # MLflow Web UI
    command: >
      mlflow server 
      --backend-store-uri sqlite:////mlflow/mlflow.db 
      --default-artifact-root /mlflow/artifacts 
      --host 0.0.0.0
    volumes:
      - ./mlflow_data:/mlflow
```

## 3. DevContainer Configuration (`devcontainer.json`)

To tell VS Code to use Docker Compose rather than building an isolated container, place a `.devcontainer/devcontainer.json` file in your repository:

```json
{
    "name": "CIS 731 OSEMN Pipeline",
    "dockerComposeFile": ["../docker-compose.yml"],
    "service": "workspace",
    "workspaceFolder": "/workspace",
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",
                "ms-toolsai.jupyter"
            ]
        }
    }
}
```

## 4. Docker Operations & Command-Line Execution

Execute the following steps in your terminal to bring up the environment, process data, and shut down cleanly.

**Step 1: Prepare Local Directories**
Because you are no longer using Databricks `/Volumes/`, you must create local directories to mount into your containers.

```bash
mkdir -p data/raw data/silver data/gold mlflow_data
```

*Place your downloaded IEEE-CIS Kaggle CSV files inside `data/raw/`.*

**Step 2: Build and Start the Cluster**
Run this from your repository root (where the `docker-compose.yml` lives) to build the updated `Dockerfile` and start all services in the background.

```bash
docker compose up -d --build
```

**Step 3: Verify Running Services**
Check that the workspace, master, two workers, and MLflow server are all running.

```bash
docker compose ps
```

You can now access:

* **Spark Master UI:** `http://localhost:8080`
* **MLflow Tracking UI:** `http://localhost:5000`

**Step 4: Attach VS Code**

1. Open VS Code.
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac).
3. Type and select **Dev Containers: Reopen in Container**.
4. VS Code will attach to the `cis731-workspace` container. When you execute PySpark code connecting to `spark://spark-master:7077`, the heavy lifting is physically routed to `spark-worker-1` and `spark-worker-2`.

**Step 5: Teardown**
When finished, shut down the cluster and release system memory. The `-v` flag removes temporary network bridges, but your mapped `./data/` and `./mlflow_data/` volumes remain safely on your host drive.

```bash
docker compose down
```
