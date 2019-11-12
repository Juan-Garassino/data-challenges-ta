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


def predict_local(X_test):
    """Send json data to a deployed model for prediction. """
    # Get model.joblib file you saved lacally from last exercice and load it
    # Compute predictiions
    return predictions


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


def evaluate_model(y, y_pred):
    # Fill that one here, how do you evaluate a regressor ?
    return res


if __name__ =='__main__':
    df = get_test_data().head(1000)
    X_test, y_test = preprocess(df)
    results = predict_local(X_test)
    df["fare_predicted"] = results
    print(evaluate_model(y_test, df.fare_predicted))
    df.to_csv("predictions.csv")
