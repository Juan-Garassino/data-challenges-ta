import datetime
from math import radians, cos, sin, asin, sqrt

import pandas as pd


# ---------------------------------------
# Here your sandbox for preprocessing
# ---------------------------------------
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


def add_distance(df):
    df['dist'] = df.apply(
        lambda x: haversine_dist(x.pickup_latitude, x.pickup_longitude, x.dropoff_latitude, x.dropoff_longitude),
        axis=1)
    return df


def treat_time(df):
    df['pickup_datetime'] = df['pickup_datetime'].apply(pd.to_datetime)
    df['pickup_day'] = df['pickup_datetime'].apply(lambda x: x.day)
    return df


# --------------------------------------------
# Here the function you'll call for your model
# --------------------------------------------
def global_preprocessing(df):
    """
    function to call
    :param df: raw input before any preprocessing
    :return: X, y for training or evaluation
    """
    df = treat_time(df)
    df = add_distance(df)
    df = df.drop(columns=['pickup_datetime', 'key'], axis=1)
    y = df.pop('fare_amount')
    X = df
    return X, y
