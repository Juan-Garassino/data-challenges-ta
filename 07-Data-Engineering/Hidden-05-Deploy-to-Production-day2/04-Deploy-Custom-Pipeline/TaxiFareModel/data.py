import pandas as pd

from google.cloud import storage

BUCKET_NAME = "wagon-ml-bizot-27"
PATH_INSIDE_BUCKET = "data/data_10Mill.csv"


def get_data(nrows=10000):
    """method to get the training data (or a portion of it) from google cloud bucket"""
    # don't forget to add Add stroage.Client() 
    return df


def clean_df(df, test=False):
    df = df.dropna(how='any', axis='rows')
    df = df[(df.dropoff_latitude != 0) | (df.dropoff_longitude != 0)]
    df = df[(df.pickup_latitude != 0) | (df.pickup_longitude != 0)]
    if "fare_amount" in list(df):
        df = df[df.fare_amount.between(0, 4000)]
    df = df[df.passenger_count < 8]
    df = df[df.passenger_count >= 0]
    df = df[df["pickup_latitude"].between(left=40, right=42)]
    df = df[df["pickup_longitude"].between(left=-74.3, right=-72.9)]
    df = df[df["dropoff_latitude"].between(left=40, right=42)]
    df = df[df["dropoff_longitude"].between(left=-74, right=-72.9)]
    return df
