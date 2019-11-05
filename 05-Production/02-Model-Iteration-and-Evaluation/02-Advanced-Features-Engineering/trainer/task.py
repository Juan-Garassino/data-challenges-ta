# Standard python import
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
from termcolor import colored
# from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor

pd.options.mode.chained_assignment = None  # default='warn'

from sklearn.pipeline import FeatureUnion
from trainer.tools import perf_eval_regression
from trainer.pipeline_blocs import TimeFeatures, DistanceFeature

# from trainer.pipeline_blocs import Preprocessing

BUCKET_NAME = "wagon-ml"


def get_data(filename):
    """
    Get the data from Google File Storage into as a pandas DataFrame
    Help here https://googleapis.dev/python/storage/latest/index.html
    """
    df = pd.read_csv("gs://{}/data/{}".format(BUCKET_NAME, filename))
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
            ("distance", distance_feature),
            ("time_features", TimeFeatures(time_column="pickup_datetime")),
        ])
         ),
        ('inputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
        ('clf', clf)
    ])


def save_pipeline(pipeline):
    """ it should save model to .joblib file """
    pass


def evaluate_pipeline(pipeline):
    print("evaluate pipeline on test set...")
    df_test = get_data(filename='taxi_trips_test_set.csv')
    df_test = df_test.head(1000)  # keeps first X rows
    results = perf_eval_regression(pipeline, df_test, df_test.fare_amount)
    return results


if __name__ == '__main__':
    df = get_data("taxi_trips_train_sample_set.csv")
    pipeline = build_pipeline()
    pipeline.fit(X=df, y=df.fare_amount)
    save_pipeline(pipeline)
    results = evaluate_pipeline(pipeline)
    for measure, value in results.items():
        print(colored('  {}: {} '.format(measure, value), 'blue'))
