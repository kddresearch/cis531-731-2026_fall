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
```

### Step 2: Replacing Databricks `dbutils`, Unity Volumes, and `spark.read`

In Databricks, your student used Unity Catalog volume paths (`/Volumes/workspace/default/ieee_fraud_bronze/raw`) and `dbutils.secrets`. Locally, data is loaded from a local directory, and Spark is connected to the local standalone cluster.

#### **Databricks Original (`obtain.ipynb` / `scrub.ipynb`):**

```python
# Databricks-specific paths and secrets
token = dbutils.secrets.get(scope="kaggle", key="api_token")
BRONZE = "/Volumes/workspace/default/ieee_fraud_bronze/raw"

train_tx = spark.read.option("header", True).csv(f"{BRONZE}/train_transaction.csv")
```

#### **Local PySpark Port (`main.py` or Jupyter in DevContainer):**

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize Spark Session connected to local standalone cluster
spark = SparkSession.builder \
    .appName("IEEE-CIS-Fraud-Local-Port") \
    .master("spark://spark-master:7077") \
    .config("spark.executor.memory", "2g") \
    .config("spark.cores.max", "2") \
    .getOrCreate()

# Local data path mapped via Docker volumes
BRONZE = "/opt/bitnami/spark/data/raw"

# Read CSV with explicit schema handling (avoiding inferSchema timeout on 651MB CSV)
train_tx = (
    spark.read
    .option("header", True)
    .option("inferSchema", False)
    .csv(f"{BRONZE}/train_transaction.csv")
)

print(f"Successfully loaded train transactions: {train_tx.count():,} rows")
```

---

## 4. Measuring Speedup Across 1–4 Workers (The Core Requirement)

To satisfy the course requirement of evaluating parallel execution, your student can write a timing harness that adjusts the number of spark partitions and worker cores, measuring wall-clock time for an intensive map/aggregation operation (such as the missing-value profiler or type-casting scrub logic from `scrub.ipynb`).

```python
import time

def benchmark_pipeline(num_workers, num_partitions):
    # Reconfigure Spark parallelism dynamically
    spark.conf.set("spark.default.parallelism", str(num_partitions))
    spark.conf.set("spark.sql.shuffle.partitions", str(num_partitions))
    
    start_time = time.time()
    
    # Example compute-heavy operation from scrub.ipynb:
    # Profiling missing values across all columns of train_transaction
    total_rows = train_tx.count()
    missing_exprs = [
        F.sum(F.when(F.col(c).isNull() | (F.trim(F.col(c)) == ""), 1).otherwise(0)).alias(c)
        for c in train_tx.columns[:50] # Bounded to 50 columns for local RAM safety
    ]
    
    summary = train_tx.agg(*missing_exprs).collect()
    
    elapsed = time.time() - start_time
    print(f"[Workers: {num_workers} | Partitions: {num_partitions}] Completed in {elapsed:.2f} seconds")
    return elapsed

# Execute scaling benchmark
t1 = benchmark_pipeline(num_workers=1, num_partitions=2)
t2 = benchmark_pipeline(num_workers=2, num_partitions=4)
t4 = benchmark_pipeline(num_workers=2, num_partitions=8)

print(f"\nSpeedup (2 partitions vs 4 partitions): {t1 / t2:.2f}x")
```

### Summary of Local Migration Benefits

By shifting from the Databricks Free Tier to a local Docker DevContainer and multi-container Spark setup:

* **Timeouts are eliminated** because there are no idle shutoffs or cloud gateway limits.
* **Data locality is preserved** by storing the IEEE-CIS CSV files directly in `./data/raw`.
* **Exact PySpark syntax is maintained**, meaning zero code rewrites are required for `.groupBy()`, `.withColumn()`, join logic, or Delta/Parquet writes.
