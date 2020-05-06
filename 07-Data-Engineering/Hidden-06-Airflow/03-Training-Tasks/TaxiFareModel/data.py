import pandas as pd
from google.cloud import storage
from TaxiFareModel.utils import simple_time_tracker

BUCKET_NAME = "wagon-ml-bizot-27"
PATH_INSIDE_BUCKET = "data/data_10Mill.csv"

DIST_ARGS = dict(start_lat="pickup_latitude",
                 start_lon="pickup_longitude",
                 end_lat="dropoff_latitude",
                 end_lon="dropoff_longitude")


@simple_time_tracker
def get_data_from_bq(N=10000, test=False, all=False, clean=True):
    from google.cloud import bigquery
    """
    qeury data from BQ and return data as dataframe
    :param N: number of rows to query
    :param test: get test data if set to True
    :return: DataFrame
    """
    client = bigquery.Client()
    table = 'wagon-bootcamp-256316.taxifareEU.taxi_trips_weather'
    # write sql query here
    TEST = "true" if test else "false"
    sql = """
    SELECT * FROM `{}` where test={} LIMIT {}
    """.format(table, TEST, N)
    if all:
        sql = """
        SELECT * FROM `{}` where test={}
        """.format(table, TEST)
    df = client.query(sql).result().to_dataframe()
    df.drop("test", axis=1, inplace=True)
    if clean:
        df = clean_df(df, test=test)
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
