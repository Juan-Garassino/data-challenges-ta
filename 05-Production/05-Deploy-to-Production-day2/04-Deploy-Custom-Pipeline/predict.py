from math import sqrt
import os
import pandas as pd
import googleapiclient.discovery
from sklearn.metrics import mean_absolute_error, mean_squared_error

BUCKET_NAME = "wagon-ml"


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


def get_data(filename):
    """ load test data """
    return pd.read_csv("gs://%s/data/%s" % (BUCKET_NAME, filename))


def convert_to_json_instances(X_test):
    return X_test.to_dict(orient="records")


def evaluate_model(y, y_pred):
    MAE = round(mean_absolute_error(y, y_pred), 2)
    RMSE = round(sqrt(mean_squared_error(y, y_pred)), 2)
    res = {'MAE': MAE, 'RMSE': RMSE}
    return res


if __name__ == '__main__':
    pipeline_version="YOUR_VERSION_NAME"
    df = get_data("taxi_trips_test_set.csv").head(1000)
    instances = convert_to_json_instances(df)
    results = predict_json(project='wagon-bootcamp-256007',
                           model='taxi_fare_prediction_model',
                           instances=instances, version=pipeline_version)

    df["fare_predicted"] = results
    print(evaluate_model(df.fare_amount, df.fare_predicted))
