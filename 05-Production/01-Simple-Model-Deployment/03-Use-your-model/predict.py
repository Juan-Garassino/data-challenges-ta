from math import sqrt
import os
import pandas as pd
from google.cloud import storage
import googleapiclient.discovery
from sklearn.metrics import mean_absolute_error, mean_squared_error

PROJECT_ID="xxx"
BUCKET_NAME = "wagon-ml"
FILEMAME = "/data/taxi_trips_test_set.csv"
BUCKET = storage.Client().bucket(BUCKET_NAME)

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
    blob = BUCKET.blob(FILEMAME)
    blob.download_to_filename(FILEMAME)
    with open(FILEMAME, 'r') as train_data:
        df = pd.read_csv(train_data)
    os.remove(FILEMAME)
    return df


def preprocess(df):
    """
    preprocess method. This should be identical to the preprocess method
    that was used from training.
    """
    df = df[FEATURES + ["fare_amount"]].dropna()
    y_test = df["fare_amount"]
    X_test = df[FEATURES]
    return X_test, y_test


def convert_to_json_instances(X_test):
    return X_test.values.tolist()


def evaluate_model(y, y_pred):
    MAE = round(mean_absolute_error(y, y_pred), 2)
    RMSE = round(sqrt(mean_squared_error(y, y_pred)), 2)
    res = {'MAE': MAE, 'RMSE': RMSE}
    return res


# only predict for the first 10 rows
df = get_test_data().head(10)
X_test, y_test = preprocess(df)
instances = convert_to_json_instances(X_test)
results = predict_json(project=PROJECT_ID,
                       model='taxi_fare_prediction_model',
                       instances=instances, version=None)

df["fare_predicted"] = results
print(evaluate_model(y_test, df.fare_predicted))
df.to_csv("predictions.csv")
