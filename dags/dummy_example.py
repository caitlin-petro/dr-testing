from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator

default_args = {
    "owner": "airflow",
    "retries": 0,
}

with DAG(
    dag_id="dummy_example",
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",   # runs daily
    catchup=False,
    tags=["example", "dummy"],
) as dag:

    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    start >> end
