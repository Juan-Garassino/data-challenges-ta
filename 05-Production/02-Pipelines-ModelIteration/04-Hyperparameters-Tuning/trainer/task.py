# Standard python import
import numpy as np
import pandas as pd
from google.cloud import storage
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.externals import joblib
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from termcolor import colored

pd.options.mode.chained_assignment = None  # default='warn'
from sklearn.pipeline import FeatureUnion
from trainer.tools import perf_eval_regression
from trainer.pipeline_blocs import TimeFeatures, DistanceFeature

from sklearn.model_selection import GridSearchCV

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
            ("time_features", TimeFeatures(time_column="pickup_datetime")),
            ("distance", distance_feature)])),
        ('inputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
        ('clf', clf)
    ])


def fit_with_grid_search(pipeline, X, y):
    """
        Use grid search to improve training parameters.
    """
    # Implement GridSearchCV Here with correct parameter range choice
    CV = "Fill_Here"
    CV.fit(X, y)
    print(CV.best_params_)
    return CV


def save_pipeline(pipeline):
    model_name = 'model.joblib'
    joblib.dump(pipeline, model_name)

    client = storage.Client().bucket(BUCKET_NAME)
    blob = client.blob('{}/{}/{}/{}'.format(
        'models',
        'taxi_fare_model',
        'pipeline_v2_with_grid_search',
        model_name))
    blob.upload_from_filename(model_name)


def evaluate_pipeline(pipeline):
    print("evaluate pipeline on test set...")
    df_test = get_data(filename='taxi_trips_test_set.csv')
    df_test = df_test.head(1000)  # keeps first X rows
    results = perf_eval_regression(pipeline, df_test, df_test.fare_amount)
    return results


if __name__ == '__main__':
    df = get_data("taxi_trips_train_sample_set.csv")
    pipeline = build_pipeline()
    pipeline = fit_with_grid_search(pipeline, X=df, y=df.fare_amount)
    save_pipeline(pipeline)
    results = evaluate_pipeline(pipeline)
    for measure, value in results.items():
        print(colored('  {}: {} '.format(measure, value), 'blue'))
