from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class TimeFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, time_column, time_zone_name='America/Los_Angeles'):
        self.time_column = time_column
        self.time_zone_name = time_zone_name

    def transform(self, X, y=None):
        assert isinstance(X, pd.DataFrame)

        X.index = pd.to_datetime(X[self.time_column])
        X.index = X.index.tz_convert(self.time_zone_name)
        X["dow"] = X.index.weekday
        X["hour"] = X.index.hour
        X["month"] = X.index.month
        X["year"] = X.index.year
        return X[["dow", "hour", "month", "year"]].reset_index(drop=True)

    def fit(self, X, y=None):
        return self

class DistanceFeature(BaseEstimator, TransformerMixin):

    def __init__(self, 
                 start_lat="start_lat", 
                 start_lon="start_lon", 
                 end_lat="end_lat", 
                 end_lon="end_lon",
                 distance_type="haversine"):
        self.distance_type = distance_type
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.end_lat = end_lat
        self.end_lon = end_lon

    def transform(self, X, y=None):
        assert isinstance(X, pd.DataFrame)

        X["distance"] = haversine_vectorized(X, 
            start_lat=self.start_lat,
            start_lon=self.start_lon,
            end_lat=self.end_lat,
            end_lon=self.end_lon,
        )
        return X[["distance"]]

    def fit(self, X, y=None):
        return self

def haversine_vectorized(df, 
    start_lat="start_lat", 
    start_lon="start_lon", 
    end_lat="end_lat", 
    end_lon="end_lon"):

    """ 
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees).
        Vectorized version of the haversine distance for pandas df
        Computes distance in kms
    """

    lat_1_rad, lon_1_rad = np.radians(df[start_lat].astype(float)), np.radians(df[start_lon].astype(float))
    lat_2_rad, lon_2_rad = np.radians(df[end_lat].astype(float)), np.radians(df[end_lon].astype(float))
    dlon = lon_2_rad - lon_1_rad
    dlat = lat_2_rad - lat_1_rad

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat_1_rad) * np.cos(lat_2_rad) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    haversine_distance = 6371 * c
    
    return haversine_distance

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
        X = X.drop('key', axis=1)
        return X

    def fit(self, X, *optional_list, **optional_dict):
        return self


class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        assert isinstance(X, pd.DataFrame)

        try:
            return X[self.columns]
        except KeyError:
            cols_error = list(set(self.columns) - set(X.columns))
            raise KeyError("The DataFrame does not include the columns: {}".format(cols_error))
