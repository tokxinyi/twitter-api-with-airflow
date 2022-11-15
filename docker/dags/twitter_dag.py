from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from twitter_etl import etl

with DAG('twitter_dag', schedule_interval='@daily', start_date=datetime(2022,11,10), catchup=False, tags=['twitter_api']) as dag:

    run_etl = PythonOperator(
        task_id='etl',
        python_callable=etl
    )

    run_etl