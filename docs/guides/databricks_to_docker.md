# CIS 731: Databricks Service Analysis & Docker DevContainer Porting Guide

## 1. Databricks Service Analysis: Timeout Diagnosis

When using the **Databricks Community Edition (Free Tier)**, frequent notebook timeouts, cluster termination, and gateway errors are caused by **strict platform resource limits and idle-timeout policies**, rather than permanent service expiration or random infrastructural brownouts. 

Specifically, the free tier enforces three operational constraints:
1. **Idle Cluster Termination:** Free-tier clusters automatically terminate after **120 minutes of inactivity** (no active notebook cell execution), wiping out temporary workspace state and mounted DBFS/Unity Catalog caches.
2. **Driver Node Memory & CPU Caps:** Free clusters run on severely constrained single-node or minimal shared-driver configurations (typically 15 GB RAM / 2 vCPUs). Heavy memory operations—such as broadcasting large joins, collecting multi-gigabyte DataFrames (`df.collect()`), or running unoptimized `.csv` inferSchema scans over the 651 MB `train_transaction.csv` file—trigger Java Out-of-Memory (OOM) errors on the driver, causing the Databricks web UI to lose connection and report a gateway timeout.
3. **Shared Control Plane Load:** During peak academic or regional usage hours, community edition shared control planes experience queue contention, leading to RPC timeouts when starting clusters or writing Delta tables to `/Volumes/`.

---

## 2. The Exit Strategy: Porting from Databricks to a Local Docker DevContainer

To escape free-tier timeouts while fulfilling the requirement to run distributed PySpark jobs with 2–4 workers and measure speedups, students can transition to a local **VS Code DevContainer** running a containerized Apache Spark cluster.

### Architecture Comparison & Tradeoffs

| Feature | Databricks (Free Tier / Managed) | Docker DevContainer + Local PySpark |
| :--- | :--- | :--- |
| **Compute Scale** | Managed cloud cluster (Driver + Workers) | Local containerized Spark (Standalone Master + $N$ Workers) |
| **Storage & Delta Lake** | Unity Catalog Volumes (`/Volumes/`) & Delta Lake | Local file system (`./data/`, `./delta/`) & Parquet/Delta |
| **Environment Control** | Pre-baked Databricks Runtime (DBR) | Fully reproducible pinned Docker image (`Dockerfile`) |
| **Timeout Risk** | High (120-min idle limit, driver OOM limits) | Zero (bound only by local machine RAM and CPU) |
| **What You CAN Do** | Execute distributed Spark SQL, Delta Lake, and MLflow logging | Run local multi-node Spark (`spark://host:port`), partition data across 2–4 local worker threads/containers, benchmark scale-up speedups, and run unit tests |
| **What You CANNOT Do** | Utilize managed serverless compute, enterprise Unity Catalog governance, or multi-terabyte auto-scaling clusters without paid cloud credits | Run on cloud object storage without local mount configuration; limited by host machine RAM |

---

## 3. Fully Detailed Porting Guide & Code Examples

### Step 1: Docker Compose Setup for Local PySpark (1 Master, 2–4 Workers)

Create a `docker-compose.yml` in your project root to spin up a local Spark cluster. This gives your student the exact multi-node architecture needed to test 2–4 worker partitions and measure speedups.

```yaml
version: '3.8'

services:
  spark-master:
    image: bitnami/spark:3.5
    container_name: spark-master
    environment:
      - SPARK_MODE=master
      - SPARK_MASTER_HOST=spark-master
    ports:
      - "8080:8080"
      - "7077:7077"
    volumes:
      - ./data:/opt/bitnami/spark/data

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
