import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class TimeFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, time_column, time_zone_name='America/Los_Angeles'):
        """
        NB : take into account time_zone_name into your Feature Engineering if you can
        """
        self.time_column = time_column
        self.time_zone_name = time_zone_name

    def transform(self, X, y=None):
        assert isinstance(X, pd.DataFrame)

        # X["dow"] =
        # X["hour"] =
        # X["month"] =
        # X["year"] =
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

        X["distance"] = haversine(X,
                                  start_lat=self.start_lat,
                                  start_lon=self.start_lon,
                                  end_lat=self.end_lat,
                                  end_lon=self.end_lon)
        return X[["distance"]]

    def fit(self, X, y=None):
        return self


def haversine(df,
              start_lat="start_lat",
              start_lon="start_lon",
              end_lat="end_lat",
              end_lon="end_lon"):
    """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees).
        Computes distance in kms
    """
    return haversine_distance
