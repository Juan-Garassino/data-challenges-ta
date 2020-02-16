# Objective

Deploy, train and use your pipeline model with GCP  
You've trained and evaluated your first Pipeline on your laptop, now you'll do everyhting on GCP.    

## Complete TaxiFareModel/trainer.py to be trainable and deployable to GCP
Here we go back with pipeline from day3 with our custom encoders.

Modify `get_data()` function and add a `save_model()` method inside `trainer.py` in order for our class to get data from storage and to uplaod model to Stroage juste like last exercice

Take a step back and ask your self what information is now stored inside our `model.joblib` ?

Now we have the `preprocessing` and `model` information stored in our model.joblib_ object. There's one last task to complete : our preprocessing step takes pandas dataframes as input, whereas the GCP only allows json representation of our input ([see documentation](https://cloud.google.com/ml-engine/docs/v1/predict-request))  
Therefore, we will create a custom predictor class that will convert input as a pandas dataframe when predicting, and feed our model the correct input data. This custom layer allows us to be much more flexible on the input data expected for the prediction.

In this exercise, you will see how to implement the custom prediction class to leverage the use of sklearn pipelines.


## Train your model on GCP

- Edit the Makefile and run `make gcp_submit_training` to train your model on GCP.

**NB: Check that all the dependencies are inside the setup.py file**

## Create the model version with the required dependencies

For the prediction service to work, you will need to make sure the prediction service has all the code associated with your custom pipeline.

Also, you will probably need a custom predictor Class.  
For a thourough explanation about Custom Predictors please refer to [documentation](https://cloud.google.com/ml-engine/docs/custom-prediction-routines)

For this:
- Inspect `predictor.py` to make sure you feed the correct inputs to your pipeline
- Why did we implement this custom class predictor ? Ask Teacher if needed
- check that `setup.py` integrates `predictor.py` script
- Edit Makefile and run `make build_dep upload_dep` to build and package your custom code dependencies

Now create a new model version, you did it from the console before, you'll learn how to do it pragammatically now.  

Open Makefile, inspect it, and run `make create_pipeline_version` to create a new model version. Please make sure to edit the command with the right env variables:
- Why do we specify `--prediction-class` and `--package-uris` ?

## Make predictions

Now, get `predict.py` from last exercice.

You will need to change a few things, take time check the 3 steps below and understand why you do so:
- Update the format you send to google api client:
```python
def convert_to_json_instances(X_test):
    return X_test.values.tolist()
```
to 
```python
def convert_to_json_instances(X_test):
    return X_test.to_dict(orient="records")
```
- Remove the preprocessing step
- Dont forget to call `clean_df()` if you called it before your training task 

Now you can use your `predict.py` to get your predictions

## Useful documentation for this exercise
https://cloud.google.com/ml-engine/docs/scikit/custom-prediction-routine-scikit-learn
