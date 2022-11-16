import tweepy
import pandas as pd
import credentials
from datetime import datetime


def extract_data():
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

def process_data(tweets):
    # tweets in dataframe - process
    df = pd.DataFrame.from_dict(tweets.data)
    return df

def store_data(df):
    # output dataframe to csv - store data
    timestamp = datetime.today().strftime('%Y%m%d')
    s3_bucket = 'twitter-api-airflow'
    df.to_csv(f"s3://{s3_bucket}/user_tweets_{timestamp}.csv")