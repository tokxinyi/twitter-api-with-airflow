from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from twitter_etl import *

with DAG('twitter_dag', schedule_interval='@daily', start_date=datetime(2022,11,10), catchup=False, tags=['twitter_api']) as dag:

    extract_tweets = PythonOperator(
        task_id='extract_tweets',
        python_callable=extract_data
    )

    process_tweets = PythonOperator(
        task_id = 'process_tweets',
        python_callable=process_data
    )

    store_tweets = PythonOperator(
        task_id = 'store_tweets',
        python_callable = store_data
    )

    extract_tweets >> process_tweets >> store_tweets