from math import radians, cos, sin, asin, sqrt

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import mean_absolute_error, mean_squared_error


def perf_eval_regression(model, X, y):
    MAE = round(mean_absolute_error(y, model.predict(X)), 2)
    RMSE = round(sqrt(mean_squared_error(y, model.predict(X))), 2)
    res = {'MAE': MAE, 'RMSE': RMSE}
    return res


# ----------------------------------
# TIME Preprocessing
# ----------------------------------

def treat_time(df):
    """
    Feature Engineering on pickup_datetime, feel free to complete
    :param df:
    :return:
    """
    df['pickup_datetime'] = df['pickup_datetime'].apply(pd.to_datetime)
    df['pickup_hour'] = df['pickup_datetime'].apply(lambda x: x.day)
    df['pickup_dow'] = df['pickup_datetime'].apply(lambda x: x.day)
    df['pickup_month'] = df['pickup_datetime'].apply(lambda x: x.day)
    df = df.drop('pickup_datetime', axis=1)
    return df


# ----------------------------------
# Lat, Lng Preprocessing
# ----------------------------------

def add_distance(df):
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

    df['dist'] = df.apply(
        lambda x: haversine_dist(x.pickup_latitude, x.pickup_longitude, x.dropoff_latitude, x.dropoff_longitude),
        axis=1)
    return df


# ----------------------------------
# Pipeline Blocs HERE
# ----------------------------------
class FillNa(BaseEstimator, TransformerMixin):

    def transform(self, X, *optional_list, **optional_dict):
        non_numerics_columns = X.columns.difference(X._get_numeric_data().columns)
        for column in X.columns:
            if column in non_numerics_columns:
                X.loc[:, column] = X.loc[:, column].fillna(X[column].value_counts().idxmax())
            else:
                X.loc[:, column] = X.loc[:, column].fillna(X.loc[:, column].mean())
        return X

    def fit(self, X, *optional_list, **optional_dict):
        return self


class My_preprocessing(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass

    def transform(self, X, *optional_list, **optional_dict):
        X = treat_time(X)
        X = add_distance(X)
        X = X.drop('key', axis=1)
        return X

    def fit(self, X, *optional_list, **optional_dict):
        return self
