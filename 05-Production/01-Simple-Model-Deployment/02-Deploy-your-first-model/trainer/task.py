import datetime

from google.cloud import storage
from sklearn.externals import joblib

BUCKET_NAME = "wagon-ml"
FILEMAME = "XXX"

FEATURES = ['pickup_latitude', 'pickup_longitude',
            'dropoff_latitude', 'dropoff_longitude',
            'passenger_count']

BUCKET = storage.Client().bucket(BUCKET_NAME)


def get_data():
    """
    Get the data from Google File Storage, download it, save it to local, then read it into pandas DataFrame
    Help here https://googleapis.dev/python/storage/latest/index.html
    Or even simplier by using only pandas
    """
    # Complete HERE
    return df


def preprocess(df):
    """
    Preprocess the data to make it compatible with sklearn estimator
    """
    df = df[FEATURES + ["fare_amount"]].dropna()
    y_train = df["fare_amount"]
    X_train = df[FEATURES]
    return X_train, y_train


def train_model(X_train, y_train):
    """
    Chose your model and fit it
    Fit the model
    return model fitted
    """
    # Complete HERE
    return regressor


def save_model(regressor):
    """
    Save the model into a .joblib and upload it on Google Storage.
    """
    model_name = 'model.joblib'
    joblib.dump(regressor, model_name)

    client = storage.Client().bucket(BUCKET_NAME)
    blob = client.blob('{}/{}/{}/{}'.format(
        'models',
        'taxi_fare_model',
        datetime.datetime.now().strftime('%Y%m%d_%H%M%S'),
        model_name))
    blob.upload_from_filename(model_name)


df = get_data()
X_train, y_train = preprocess(df)
clf = train_model(X_train, y_train)
save_model(clf)
