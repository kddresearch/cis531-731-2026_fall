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

### Addendum 1: Host Assumptions & Docker Desktop Resource Limits

This architecture is designed entirely for **local laptops**; it does not assume an AWS host. However, running a Workspace, a Spark Master, two Spark Workers (at 2GB RAM each), and an MLflow server concurrently requires significant local memory. 

By default, Docker Desktop on macOS limits its underlying VM to 2GB or 4GB of RAM, which will cause the containers to OOM-kill immediately. 

**Required Docker Desktop Actions for Both OSes:**
1. Open Docker Desktop -> **Settings** (Gear icon).
2. Navigate to **Resources** (or Settings -> Advanced).
3. **Memory Allocation:** Increase the memory limit to **at least 8 GB** (12 GB+ recommended).
4. **CPU Allocation:** Allocate at least 4-6 virtual CPUs.
5. Apply and restart Docker Desktop.

---

### Addendum 2: Windows 11 & WSL 2 Bridgework

A "bare" WSL 2 instance (manually running `dockerd` via `systemctl` inside Ubuntu) works but creates severe friction for VS Code DevContainers, as the Windows-side VS Code struggles to automatically find the Unix Docker socket. The frictionless path is **Docker Desktop for Windows with the WSL 2 backend**.

**Windows 11 Student Instructions:**
1. Install Docker Desktop and ensure **Settings > General > "Use the WSL 2 based engine"** is checked.
2. Under **Settings > Resources > WSL Integration**, toggle the switch ON for your specific Linux distro (e.g., `Ubuntu-24.04`).
3. **CRITICAL PERFORMANCE PATCH:** Do **not** clone the Git repository into the Windows file system (`C:\Users\Name\project`). Docker volume mounts across the Windows/WSL boundary are catastrophically slow. Open your WSL 2 terminal and clone the repository directly into the native Linux file system (e.g., `~/projects/cis731-term-project`).
4. Launch VS Code from inside the WSL 2 terminal by typing `code .` in the project directory, then accept the prompt to "Reopen in Container".

---

### Addendum 3: macOS Bridgework (Apple Silicon vs. Intel)

**macOS Student Instructions:**
1. Install Docker Desktop for Mac.
2. Ensure you have completed the memory limit increase (Addendum 1).
3. **Apple Silicon (M1/M2/M3) Patch:** The `bitnami/spark:3.5` image and `python:3.10-slim-bullseye` both natively support ARM64. However, some deep PyPI dependencies (like older versions of `xgboost` or `faiss-cpu`) occasionally fail to compile on ARM. If the student on macOS encounters `faiss-cpu` architecture build errors during the `docker compose build` step, they have two options:
   * **Option A (Rosetta):** Go to Docker Desktop -> **Settings > Features in development** and enable **"Use Rosetta for x86/amd64 emulation on Apple Silicon"**. 
   * **Option B (Compose Override):** Add `platform: linux/amd64` to the `workspace` service in the `docker-compose.yml` to force x86 emulation for the Python environment.

---

### Patch 1: `docker-compose.yml` Resource Binding

If the laptops have limited RAM, the Spark workers in the original `docker-compose.yml` might try to steal resources from the workspace container. Add explicit Docker memory limits to the `docker-compose.yml` services to prevent the Spark workers from freezing the host OS:

```yaml
# Add this block to spark-worker-1 and spark-worker-2 in docker-compose.yml
    deploy:
      resources:
        limits:
          memory: 2.5G # Hard cap Docker to prevent host OS freeze
