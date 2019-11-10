# Standard python import
import pandas as pd
import numpy as np
import datetime
import os
from google.cloud import storage
from sklearn.externals import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
from termcolor import colored
from sklearn.ensemble import GradientBoostingRegressor

pd.options.mode.chained_assignment = None  # default='warn'
from google.cloud import bigquery
from sklearn.pipeline import FeatureUnion
from trainer.tools import perf_eval_regression
from trainer.pipeline_blocs import TimeFeatures, DistanceFeature

# from trainer.pipeline_blocs import Preprocessing

BUCKET_NAME = "wagon-data"


def get_data_from_bq(N=10000, test=False, all=True):
    """
    qeury data from BQ and return data as dataframe
    :param N: number of rows to query
    :param test: get test data if set to True
    :return: DataFrame
    """
    client = bigquery.Client()

    # write sql query here
    TEST = "true" if test else "false"
    sql = """
    SELECT * FROM `wagon-bootcamp-256007.ml_week_05.taxi_trips` where test={} LIMIT {}
    """.format(TEST, N)
    if all:
        sql = """
        SELECT * FROM `wagon-bootcamp-256007.ml_week_05.taxi_trips` where test={}
        """.format(TEST)
    df = client.query(sql).result().to_dataframe()
    return df


def build_pipeline():
    """
    Returns a sklearn pipeline
    """
    distance_feature = DistanceFeature(
        start_lat="pickup_latitude", start_lon="pickup_longitude",
        end_lat="dropoff_latitude", end_lon="dropoff_longitude",

    )
    clf = GradientBoostingRegressor(n_estimators=100, verbose=1)

    return Pipeline([
        ('features', FeatureUnion([
            ("time_features", TimeFeatures(time_column="pickup_datetime")),
            ("distance", distance_feature)
        ])
         ),
        ('inputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
        ('clf', clf)
    ])


def save_pipeline(pipeline, uplaod=True):
    model_name = 'model.joblib'
    joblib.dump(pipeline, model_name)

    PIPELINE_NAME = "pipeline_v3_bq_all"
    if uplaod:
        client = storage.Client().bucket(BUCKET_NAME)
        blob = client.blob('{}/{}/{}/{}'.format(
            'models',
            'taxi_fare_model',
            PIPELINE_NAME,
            model_name))
        blob.upload_from_filename(model_name)


def evaluate_pipeline(pipeline):
    print("evaluate pipeline on test set...")
    df_test = get_data_from_bq(filename='taxi_trips_test_set.csv')
    df_test = df_test.head(1000)  # keeps first X rows
    results = perf_eval_regression(pipeline, df_test, df_test.fare_amount)
    return results


if __name__ == '__main__':
    df = get_data_from_bq(all=True)
    pipeline = build_pipeline()
    y = df.pop('fare_amount')
    X = df
    pipeline.fit(X=X, y=y)
    save_pipeline(pipeline)
