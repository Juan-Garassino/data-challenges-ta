# Standard python import
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from termcolor import colored
from xgboost import XGBRegressor

pd.options.mode.chained_assignment = None  # default='warn'

# Homemade custom imports
from trainer.tools import perf_eval_regression


# ----------------------------------
# Load Data Here (to Complete
# ----------------------------------
# df = load_data()

# ----------------------------------
# Preprocessing
# ----------------------------------
class Preprocessing(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass

    def transform(self, X, *optional_list, **optional_dict):
        # Complete HERE
        return X

    def fit(self, X, *optional_list, **optional_dict):
        return self


# ----------------------------------
# PIPELINE
# ----------------------------------
y = df.pop("fare_amount")
X = df

X_train, X_test, y_train, y_test = train_test_split(X.copy(), y.copy(), test_size=0.2)

# Define your pipeline HERE
model_name, model = 'XGBRgressor', XGBRegressor()

pipe = Pipeline([('Preprocess_data', Preprocessing()),
                 ('Imputer', Imputer(missing_values=0,
                                     strategy="most_frequent",
                                     axis=0)),
                 (model_name, model)])

# Complete HERE to apply pipeline to training set
# XXXXX


# Evaluating perfs and printing results
results = perf_eval_regression(pipe, X_test, y_test)
print(colored('== {} ({})'.format(model_name, NAME), 'red'))
for measure, value in results.items():
    print(colored('  {}: {} '.format(measure, value), 'blue'))
