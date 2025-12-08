from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess
import os

BASE_PATH = "/opt/airflow/pipelines/orcamentos"

def run_script(script_name):

    script_path = os.path.join(BASE_PATH, script_name)
    subprocess.run(["python3", script_path], check=True)

default_args = {
    "owner": "owner",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id = "orcamentos_etl",
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 3 * * * ",
    catchup=False,
    default_args=default_args

) as dag:
    
    download_task = PythonOperator(
        task_id = "download_raw_files",
        python_callable=run_script,
        op_kwargs={"script_name": "download.py"}
    )

    extract_task = PythonOperator(
        task_id = "extract_raw_files",
        python_callable=run_script,
        op_kwargs={"script_name": "extract.py"}
    )

    clean_task = PythonOperator(
        task_id = "clean_transformed_files",
        python_callable=run_script,
        op_kwargs={"script_name":"clean.py"}
    )
    
    download_task >> extract_task >> clean_task