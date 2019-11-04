# Objective

Deploy, train and use your pipeline model with GCP.
In this exercise, you will see how to implement a custom prediction class to leverage the use of sklearn pipelines.

## Complete trainer/task.py to be trainable and deployable to GCP

Fill in `save_pipeline()` function inside `trainer/task.py`, and eventually `get_data()` if you loaded the data from you laptop previously

## Train your model on GCP

- Edit the Makefile and run `make gcp_submit_training` to train your model on GCP.

## Create the model version with the required dependencies

For the prediction service to work, you will need to make sure the prediction service has all the code associated with your custom pipeline.

Also, you will probably need a custom predictor Class.  
For a thorough explanation about Custom Predictors please refer to [documentation](https://cloud.google.com/ml-engine/docs/custom-prediction-routines)

For this:
- Inspect `predictor.py` to make sure you feed the correct inputs to your pipeline
- Why did we implement this custom class predictor ? Ask Teacher if needed
- check that `setup.py` integrates `predictor.py`
- Edit Makefile and run `make build_dep upload_dep` to build and package your custom code dependencies
- Check what happened :

```bash
ls
```

Now create a new model version, you did it from the console before, you'll learn how to do it pragammatically now.  

Open Makefile, inspect it, and run `make create_pipeline_version` to create a new model version. Please make sure to edit the command with the right env variables:
- Why do we specify `--prediction-class` and `--package-uris` ?

## Make predictions

Now, let's complete `predict.py` to use your new prediction service and make predictions on the test set. Output the performance (MAE, RMSE) of your predictions.

### References
https://cloud.google.com/ml-engine/docs/scikit/custom-prediction-routine-scikit-learn