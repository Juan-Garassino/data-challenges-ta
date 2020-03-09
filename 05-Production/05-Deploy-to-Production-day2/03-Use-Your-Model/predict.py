from math import sqrt

import googleapiclient.discovery
import numpy
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error

BUCKET_NAME = "TODO"
FEATURES = ['pickup_latitude', 'pickup_longitude',
            'dropoff_latitude', 'dropoff_longitude',
            'passenger_count']


def predict_json(project, model, instances, version=None):
    """Send json data to a deployed model for prediction. """

    service = googleapiclient.discovery.build('ml', 'v1')
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']


def get_test_data():
    """ load test data """
    return pd.read_csv("gs://%s/data/taxi_trips_test_set.csv" % (BUCKET_NAME))


def preprocess(df):
    """
    preprocess method. This should be identical to the preprocess method
    that was used from training.
    """
    pass


def convert_to_json_instances(X_test):
    """return list of dict"""
    pass


def evaluate_model(y, y_pred):
    MAE = round(mean_absolute_error(y, y_pred), 2)
    RMSE = round(sqrt(mean_squared_error(y, y_pred)), 2)
    res = {'MAE': MAE, 'RMSE': RMSE}
    return res


# only predict for the first 1000 rows
VERSION = "TODO"
PROJECT_ID = "TODO"
df = get_test_data().head(1000)
X_test, y_test = preprocess(df)
instances = convert_to_json_instances(X_test)
results = predict_json(project=PROJECT_ID,
                       model='TODO',
                       instances=instances, version=VERSION)

df["fare_predicted"] = results
print(evaluate_model(y_test, df.fare_predicted))
df.to_csv("predictions.csv")
