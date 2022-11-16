FROM apache/airflow:2.4.2
RUN pip install s3fs
RUN pip install tweepy
RUN pip install pandas
