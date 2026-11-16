import time
import pandas as pd
import mlflow
import joblib
from joblibspark import register_spark
from pyspark.sql import SparkSession

from sklearn.model_selection import cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

# 1. Initialize Local Spark Cluster & MLflow
spark = SparkSession.builder \
    .appName("IEEE-Fraud-CV-Benchmark") \
    .master("spark://spark-master:7077") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

register_spark() # Register the Spark backend for scikit-learn
mlflow.set_tracking_uri("http://mlflow-server:5000")
mlflow.set_experiment("Fraud_Detection_CV_Benchmark")

# 2. Load Data from Local Mount (Previously /Volumes/...)
# Note: For joblib-spark CV, the data is collected to Pandas first, 
# then broadcasted to executors for each fold.
BRONZE = "/opt/bitnami/spark/data/raw"
train_tx = spark.read.option("header", True).csv(f"{BRONZE}/train_transaction.csv")

# Light preprocessing (mocked for brevity) and conversion to Pandas
pdf = train_tx.select("TransactionAmt", "card1", "C1", "D1", "isFraud").dropna().toPandas()
X = pdf.drop("isFraud", axis=1)
y = pdf["isFraud"].astype(int)

# 3. Define Pipelines
pipeline_lr = Pipeline([
    ('feature_selection', SelectKBest(score_func=f_classif, k='all')),
    ('classifier', LogisticRegression(max_iter=1000))
])

pipeline_xgb = Pipeline([
    ('classifier', XGBClassifier(n_estimators=100, use_label_encoder=False, eval_metric='logloss'))
])

def benchmark_cv(pipeline, model_name, n_workers):
    """Executes 5-fold CV distributed across Spark workers and logs to MLflow."""
    mlflow.sklearn.autolog()
    
    with mlflow.start_run(run_name=f"{model_name}_{n_workers}_Workers"):
        start_time = time.time()
        
        # 4. The Magic Block: Distribute CV folds to Spark
        with joblib.parallel_backend('spark', n_jobs=n_workers):
            cv_results = cross_validate(
                pipeline, X, y, 
                cv=5, 
                scoring=['f1_macro', 'roc_auc'], 
                n_jobs=n_workers,
                return_estimator=True
            )
            
        elapsed = time.time() - start_time
        
        # Log aggregated metrics
        mlflow.log_metric("cv_mean_f1_macro", cv_results['test_f1_macro'].mean())
        mlflow.log_metric("cv_mean_roc_auc", cv_results['test_roc_auc'].mean())
        mlflow.log_metric("execution_time_seconds", elapsed)
        
        print(f"[{model_name} | Workers: {n_workers}] Completed 5-fold CV in {elapsed:.2f}s")
        print(f"Mean Macro-F1: {cv_results['test_f1_macro'].mean():.4f}")
        return elapsed

# 5. Measure Speedups
print("--- Benchmarking Logistic Regression ---")
t_lr_2 = benchmark_cv(pipeline_lr, "LogisticRegression", n_workers=2)
t_lr_4 = benchmark_cv(pipeline_lr, "LogisticRegression", n_workers=4)
print(f"LR Speedup (2 vs 4 workers): {t_lr_2 / t_lr_4:.2f}x\n")

print("--- Benchmarking XGBoost ---")
t_xgb_2 = benchmark_cv(pipeline_xgb, "XGBoost", n_workers=2)
t_xgb_4 = benchmark_cv(pipeline_xgb, "XGBoost", n_workers=4)
print(f"XGB Speedup (2 vs 4 workers): {t_xgb_2 / t_xgb_4:.2f}x")
