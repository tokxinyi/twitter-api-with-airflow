from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import dag, task
from datetime import datetime


@dag(schedule_interval='@daily', start_date = datetime(2022,11,10), catchup=False, tags='twitter_api')
def taskflow():

    @task(task_id = 'extract_tweets', retries = 3)
    def extract_data():
        import tweepy
        import credentials
        
        # connect to Twitter's API v2 using OAuth 1.0a User Context
        client = tweepy.Client(
            bearer_token = credentials.bearer_token,
            consumer_key = credentials.consumer_key,
            consumer_secret = credentials.consumer_secret,
            access_token = credentials.access_key,
            access_token_secret = credentials.access_secret
        )

        # get the user id from username
        username = 'NotionHQ'
        user_info = client.get_user(username=username)
        user_id = user_info.data.id

        # get the user's tweets
        tweets = client.get_users_tweets(id=user_id, exclude=['retweets','replies'])

        return tweets

    @task(task_id = 'process_tweets', retries = 3)
    def process_data(tweets):
        import pandas as pd
        
        # tweets in dataframe - process
        df = pd.DataFrame.from_dict(tweets.data)
        return df

    @task(task_id = 'store_tweets', retries = 3)
    def store_data(df):
        # output dataframe to csv - store data
        df.to_csv('user_tweets.csv', sep=',')
    
    store_data(process_data(extract_data()))

dag = taskflow()