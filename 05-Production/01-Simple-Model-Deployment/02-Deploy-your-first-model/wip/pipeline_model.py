import datetime
from math import radians, cos, sin, asin, sqrt

import pandas as pd
from google.cloud import storage
from sklearn import linear_model
from sklearn.externals import joblib

# Fill in your Cloud Storage bucket name
BUCKET_ID = "wagon-ml-production"

# Import Data From Google Cloud Storage
PATH = "../data/"
filename = "05_Production_TaxiFare_100000.csv"

# Public bucket holding the census data
bucket = storage.Client().bucket(BUCKET_ID)

# Path to the data inside the public bucket
data_dir = BUCKET_ID

# Download training dataset previously uploaded
#blob = bucket.blob(''.join([data_dir, filename]))
blob = bucket.blob(filename)
blob.download_to_filename(filename)

with open(filename, 'r') as train_data:
    df = pd.read_csv(train_data)

#df = pd.read_csv(PATH + filename)


# Basic Feature Engineering (time and distance) TODO : add Manhatan Distance, more time fetang, geohash,
# inspect pickup and dorpoff distribution
# col list ['fare_amount', 'key', 'pickup_datetime', 'pickup_longitude',
# 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'dist']
def haversine_dist(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


df['dist'] = df.apply(lambda x: haversine_dist(x.pickup_latitude, x.pickup_longitude, x.dropoff_latitude, x.dropoff_longitude), axis=1)

df['pickup_datetime'] = df['pickup_datetime'].apply(pd.to_datetime)
df['pickup_day'] = df['pickup_datetime'].apply(lambda x: x.day)

# drop useless columns
df = df.drop(columns=['pickup_datetime', 'key'], axis=1)
y_train = df.pop('fare_amount')
X_train = df

# Chose model
reg = linear_model.Lasso(alpha=0.1)
reg.fit(X=X_train, y=y_train)

# Export the model to a file
#BUCKET_NAME = [YOUR-BUCKET-NAME]
BUCKET_NAME = 'iotcore-example-mlengine'
model_name = 'model.joblib'
joblib.dump(reg, model_name)

# Upload the model_name to GCS
bucket = storage.Client().bucket(BUCKET_NAME)
blob = bucket.blob('{}/{}'.format(
    datetime.datetime.now().strftime('TaxiFare_%Y%m%d_%H%M%S'),
    model_name))
blob.upload_from_filename(model_name)
