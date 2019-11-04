# Standard python import
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from termcolor import colored

pd.options.mode.chained_assignment = None  # default='warn'

# Homemade custom imports
from trainer.tools import perf_eval_regression

# from trainer.pipeline_blocs import Preprocessing

BUCKET_NAME = "wagon-ml"


def get_data(filename):
    """
    Get data either from Cloud storage
    """
    df = pd.read_csv("gs://{}/data/{}".format(BUCKET_NAME, filename))
    return df


class Preprocessing(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass

    def transform(self, df, *optional_list, **optional_dict):
        """
        Use preprocessing from yesterday
        Simple Feature selection for the moment
        """
        # df = your_preprocessing(df)
        return df

    def fit(self, X, *optional_list, **optional_dict):
        return self


def build_pipeline():
    """
    Create your Pipeline HERE
    Add first two blocs (Preprocessing and Imputer)
    """
    pipeline = Pipeline([
        # Add 2 blocs HERE
        ('clf', GradientBoostingRegressor(n_estimators=100, verbose=1))
    ])
    return pipeline


def save_pipeline(pipeline):
    """ it should save model to .joblib file
    Use code from Day 1
    Two possibilities :
    1°) save it locally
    2°) upload it to cloud storage if training job computed in AI plaform"""
    pass


def evaluate_pipeline(pipeline):
    print("evaluate pipeline on test set...")
    df_test = get_data(filename="taxi_trips_test_set.csv")
    df_test = df_test.head(1000)  # keeps first X rows
    results = perf_eval_regression(pipeline, df_test, df_test.fare_amount)
    return results


if __name__ == '__main__':
    df = get_data(filename="taxi_trips_train_sample_set.csv")
    pipeline = build_pipeline()
    pipeline.fit(X=df, y=df.fare_amount)
    save_pipeline(pipeline)
    results = evaluate_pipeline(pipeline)
    for measure, value in results.items():
        print(colored('  {}: {} '.format(measure, value), 'blue'))
