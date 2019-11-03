from math import sqrt
from sklearn.metrics import mean_absolute_error, mean_squared_error


def perf_eval_regression(model, X, y):
    MAE = round(mean_absolute_error(y, model.predict(X)), 2)
    RMSE = round(sqrt(mean_squared_error(y, model.predict(X))), 2)
    res = {'MAE': MAE, 'RMSE': RMSE}
    return res


