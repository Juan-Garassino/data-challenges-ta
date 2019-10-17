from math import sqrt

import pandas as pd
from sklearn.externals import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error
from trainer.model import FEATURES

def perf_eval_regression(y_pred, y):
    MAE = round(mean_absolute_error(y, y_pred), 2)
    RMSE = round(sqrt(mean_squared_error(y, y_pred)), 2)
    res = {'MAE': MAE, 'RMSE': RMSE}
    return res


PATH = '../data/05_Production_TaxiFare_TEST_1000_with_answers.csv'
model = './model.joblib'
cols2drop = ['pickup_datetime', 'key']

test = pd.read_csv(PATH)
test = test.drop(columns=cols2drop, axis=1)

y_test = test.pop('fare_amount')
X_test = test

loaded_model = joblib.load(model)
y_pred = loaded_model.predict(X_test)
result = perf_eval_regression(y_pred, y_test)
print(result)
