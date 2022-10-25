import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import credentials



# connect to Twitter's API v2 using OAuth 1.0a User Context
client = tweepy.Client(
    bearer_token = credentials.bearer_token,
    consumer_key = credentials.consumer_key,
    consumer_secret = credentials.consumer_secret,
    access_token = credentials.access_key,
    access_token_secret = credentials.access_secret
)

