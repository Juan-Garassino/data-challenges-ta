from math import sqrt

import pandas as pd
from sklearn.externals import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error


def perf_eval_regression(y_pred, y):
    MAE = round(mean_absolute_error(y, y_pred), 2)
    RMSE = round(sqrt(mean_squared_error(y, y_pred)), 2)
    res = {'MAE': MAE, 'RMSE': RMSE}
    return res


PATH = "/Users/jeanbizot/code/lewagon/data-challenges/05-Production/01-Simple-Model-Deployment/data/"
filename = "05_Production_TaxiFare_100000.csv"
model = "./model.joblib"
df = pd.read_csv(PATH + filename)

y_test = df.pop("fare_amount")
X_test = df

loaded_model = joblib.load(model)
y_pred = loaded_model.predict(X_test)
result = perf_eval_regression(y_pred, y_test)
print(result)
