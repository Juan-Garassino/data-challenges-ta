import category_encoders as ce
import pandas as pd
from TaxiFareModel.data import get_data, clean_df, BUCKET_NAME
from TaxiFareModel.encoders import TimeFeaturesEncoder, DistanceTransformer, AddGeohash
from TaxiFareModel.utils import compute_rmse
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import Lasso, Ridge, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder
from google.cloud import storage

dist_args = dict(start_lat="pickup_latitude",
                 start_lon="pickup_longitude",
                 end_lat="dropoff_latitude",
                 end_lon="dropoff_longitude")

MODEL_VERSION = "Pipelinev0"


class Trainer(object):
    TRAINING_NROWS = 10000
    ESTIMATOR = "Lasso"
    SPLIT=False

    def __init__(self, data=None, **kwargs):
        """
        FYI:
        __init__ is called every time you instatiate Trainer
        Consider kwargs as a dict containig all possible parameters given to your constructor
        Example:
            TT = Trainer(nrows=1000, estimator="Linear")
               ==> kwargs = {"nrows": 1000,
                            "estimator": "Linear"}
        :param data:
        :param kwargs:
        """
        self.pipeline = None
        self.kwargs = kwargs
        self.nrows = kwargs.get("nrows", self.TRAINING_NROWS)  # cf doc above
        self.df = None
        if isinstance(data, pd.DataFrame):
            self.df = data

    def get_estimator(self):
        estimator = self.kwargs.get("estimator", self.ESTIMATOR)
        if estimator == "Lasso":
            model = Lasso()
        elif estimator == "Ridge":
            model = Ridge()
        elif estimator == "Linear":
            model = LinearRegression()
        elif estimator == "GBM":
            model = GradientBoostingRegressor()
        else:
            model = Lasso()
        estimator_params = self.kwargs.get("estimator_params", {})
        model.set_params(**estimator_params)
        print(model.__class__.__name__)
        return model

    def set_pipeline(self):

        time_features = make_pipeline(TimeFeaturesEncoder(time_column='pickup_datetime'),
                                      OneHotEncoder(handle_unknown='ignore'))

        pipe_geohash = make_pipeline(AddGeohash(), ce.HashingEncoder())

        dist_args = dict(start_lat="pickup_latitude",
                         start_lon="pickup_longitude",
                         end_lat="dropoff_latitude",
                         end_lon="dropoff_longitude")

        features_encoder = ColumnTransformer([
            ('distance', DistanceTransformer(**dist_args), list(dist_args.values())),
            ('time_features', time_features, ['pickup_datetime']),
            ('geohash', pipe_geohash, list(dist_args.values()))
        ])

        self.pipeline = Pipeline(steps=[
            ('features', features_encoder),
            ('rgs', self.get_estimator())])

    def evaluate(self, X_test, y_test):
        if self.pipeline is None:
            raise ("Cannot evaluate an empty pipeline")
        y_pred = self.pipeline.predict(X_test)
        return compute_rmse(y_pred, y_test)

    def train(self):
        if not isinstance(self.df, pd.DataFrame):
            self.df = get_data(nrows=100000, bq=True)
        y_train = self.df["fare_amount"]
        X_train = self.df.drop("fare_amount", axis=1)
        self.split = self.kwargs.get("split", self.TRAINING_NROWS)  # cf doc above
        if self.split:
            X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.15)
        print(X_train.shape)
        self.set_pipeline()
        self.pipeline.fit(X_train, y_train)
        if self.split:
            rmse = self.evaluate(X_val, y_val)

    #def save_model

if __name__ == "__main__":
    N = 1000
    df = get_data(nrows=N)
    df = clean_df(df)

    t = Trainer(data=df, estimator="Linear")
    t.train()
    t.save_model()
