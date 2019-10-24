import datetime

import numpy as np
import pandas as pd
from google.cloud import storage
from sklearn.externals import joblib
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from termcolor import colored
from trainer.pipeline_blocs import FillNa, My_preprocessing, perf_eval_regression
from xgboost import XGBRegressor

pd.options.mode.chained_assignment = None  # default='warn'

BUCKET_NAME = "wagon-data"
filename = "05_Production_TaxiFare_100000.csv"

bucket = storage.Client().bucket(BUCKET_NAME)
blob = bucket.blob(filename)
blob.download_to_filename(filename)
with open(filename, 'r') as train_data:
    df = pd.read_csv(train_data)

# ----------------------------------
# Preprocessing
# ----------------------------------

y = df.pop("fare_amount")
X = df

X_train, X_test, y_train, y_test = train_test_split(X.copy(), y.copy(), test_size=0.2)

# Chose model
N = 2
regressor = ('Lasso',
             Lasso(),
             {'PIPE_MODEL__alpha': [0.1],
              'PIPE_MODEL__max_iter': list(np.linspace(500, 1500, N, dtype=int))})

model_name, model_instance, params = regressor
pipe = Pipeline([('replace NaN values', FillNa()),
                 ('Preprocess_data', My_preprocessing()),
                 ('PIPE_MODEL', model_instance)])
grid = GridSearchCV(pipe, params)
grid.fit(X_train, y_train)

# Export the model to a file
model_name = 'model.joblib'
joblib.dump(grid, model_name)

# Upload the model_name to GCS
blob = bucket.blob('{}/{}'.format(
    datetime.datetime.now().strftime('TaxiFare_pipeline_%Y%m%d_%H%M%S'),
    model_name))
blob.upload_from_filename(model_name)
