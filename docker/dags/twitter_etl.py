import tweepy
import pandas as pd
import s3fs
import credentials
from datetime import datetime


def etl():
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

    # transform to a dataframe
    df = pd.DataFrame.from_dict(tweets.data)

    # instantiate s3 object
    s3 = s3fs.S3FileSystem()

    # output the dataframe to s3 bucket
    timestamp = datetime.today().strftime('%Y%m%d')
    df.to_csv(f"s3://twitter-api-airflow/user_tweets_{timestamp}.csv")
