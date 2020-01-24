from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd

def model():

    data = pd.read_csv("./cleaned_data.csv")

    X = data.iloc[:,0:5]

    y = data['y']

    model = DecisionTreeClassifier()

    scores = cross_val_score(model, X, y, cv=10)

    return round(scores.mean(),2)


