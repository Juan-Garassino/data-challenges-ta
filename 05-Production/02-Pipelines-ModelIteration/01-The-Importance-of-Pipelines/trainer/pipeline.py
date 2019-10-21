import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from termcolor import colored
from trainer.tools import FillNa, My_preprocessing, perf_eval_regression
from xgboost import XGBRegressor
pd.options.mode.chained_assignment = None  # default='warn'

NAME = "Taxi Fare Prediction"
PATH = "/Users/jeanbizot/code/lewagon/data-challenges/05-Production/01-Simple-Model-Deployment/data/"
filename = "05_Production_TaxiFare_100000.csv"
df = pd.read_csv(PATH + filename)

# ----------------------------------
# Preprocessing
# ----------------------------------

y = df.pop("fare_amount")
X = df

X_train, X_test, y_train, y_test = train_test_split(X.copy(), y.copy(), test_size=0.2)

# Chose model
N = 2
regressors = [('XGBRgressor',
               XGBRegressor(),
               {'PIPE_MODEL__nthread': [4],  # when use hyperthread, xgboost may become slower
                'PIPE_MODEL__objective': ['reg:squarederror'],
                'PIPE_MODEL__n_estimators': list(np.linspace(500, 3000, N, dtype=int))}),
              ('Lasso',
               Lasso(),
               {'PIPE_MODEL__alpha': [0.1],
                'PIPE_MODEL__max_iter': list(np.linspace(500, 1500, N, dtype=int))})]

# Testing different models
for model_name, model_instance, params in regressors:
    pipe = Pipeline([('replace NaN values', FillNa()),
                     ('Preprocess_data', My_preprocessing()),
                     ('PIPE_MODEL', model_instance)])
    grid = GridSearchCV(pipe, params)
    grid.fit(X_train, y_train)
    # Evaluating perfs and printing results
    results = perf_eval_regression(grid, X_test, y_test)
    print(colored('== {} ({})'.format(model_name, NAME), 'red'))
    for measure, value in results.items():
        print(colored('  {}: {} '.format(measure, value), 'blue'))
