import datetime
import os

import pandas as pd
from google.cloud import storage
from sklearn import linear_model
from sklearn.externals import joblib
from trainer.model import FEATURES

BUCKET_NAME = "wagon-data"
filename = "05_Production_TaxiFare_100000.csv"

bucket = storage.Client().bucket(BUCKET_NAME)
blob = bucket.blob(filename)
blob.download_to_filename(filename)
with open(filename, 'r') as train_data:
    df = pd.read_csv(train_data)
os.remove(filename)


# ----------------------------------
# Preprocessing
# ----------------------------------
def preprocess(df):
    """
    Write preprocessing function here
    :param df: raw DataFrame read from GCP Storage
    :return: X_train, y_train
    """
    cols2drop = ['pickup_datetime', 'key']
    df = df.drop(columns=cols2drop, axis=1)

    y_train = df.pop('fare_amount')
    # X_train = df[FEATURES]
    X_train = df
    return X_train, y_train


# ----------------------------------
# Use functions HERE
# ----------------------------------
X_train, y_train = preprocess(df)
# Chose model
reg = linear_model.Lasso(alpha=0.1)
reg.fit(X=X_train, y=y_train)

# Export the model to a file
model_name = 'model.joblib'
joblib.dump(reg, model_name)

# Upload the model_name to GCS
blob = bucket.blob('{}/{}'.format(
    datetime.datetime.now().strftime('TaxiFare_%Y%m%d_%H%M%S'),
    model_name))
blob.upload_from_filename(model_name)
