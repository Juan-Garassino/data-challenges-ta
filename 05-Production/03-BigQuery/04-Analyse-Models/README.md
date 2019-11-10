# Analyse your models performance

In this exercise, the goal is to build different models and compare their performance
using BigQuery and Data Studio.

## Save model predictions

Create a `batch_prediction.py` job that will:
- make predictions for the first 20 000 samples of your test set  
    => Beware here google's predictor only accepts a limited input data size 
- compute error for each prediction
- save these predictions into a new `model_predictions` table
 => Ideally this table will contain all features from test sample, the model version, the error, and the predicted values

Run this job locally.

## Analyse
- analyse results using DataStudio
- compute ME, MAE, RMSE
- look at errors distribution