import datetime

import pandas as pd
from google.cloud import storage
from sklearn import linear_model
from sklearn.externals import joblib
from trainer.model import FEATURES

# Download training dataset previously uploaded From Google Cloud Storage
BUCKET_NAME = "wagon-data"
bucket = storage.Client().bucket(BUCKET_NAME)
filename = "05_Production_TaxiFare_100000.csv"
blob = bucket.blob(filename)
blob.download_to_filename(filename)

with open(filename, 'r') as train_data:
    df = pd.read_csv(train_data)

# ----------------------------------
# Preprocessing
# ----------------------------------

y_train = df["fare_amount"]
X_train = df[FEATURES]

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
