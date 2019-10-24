from math import sqrt

import pandas as pd
from sklearn.externals import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error


def perf_eval_regression(y_pred, y):
    MAE = round(mean_absolute_error(y, y_pred), 2)
    RMSE = round(sqrt(mean_squared_error(y, y_pred)), 2)
    res = {'MAE': MAE, 'RMSE': RMSE}
    return res


PATH = '../data/05_Production_TaxiFare_TEST_1000_with_answers.csv'
model = '../02-Deploy-your-first-model/model.joblib'

df = pd.read_csv(PATH)


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


X_test, y_test = preprocess(df)

loaded_model = joblib.load(model)
y_pred = loaded_model.predict(X_test)
result = perf_eval_regression(y_pred, y_test)
print(result)
