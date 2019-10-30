# Objective

Now, your will train your first model on GCP.
The goal is to build a very simple model for the taxi fare prediction problem. The focus is to build a deployment pipeline that will be easy to iterate on and improve. We will not try to make the model accurate yet. We will make improvements later.

## Create Bucket

First, let's create a bucket that will be used to store all the models you will build.

```bash
PROJECT_ID=$(gcloud config list project --format "value(core.project)")
BUCKET_NAME=${PROJECT_ID}-models
REGION=europe-west1
gsutil mb -l $REGION gs://$BUCKET_NAME
```

## Create a Model

- go to https://console.cloud.google.com/ai-platform/models
- create a model `taxi_fare_prediction_model`

## Complete task.py

Open it and complete to train your first model on GCloud as seen in the course.

## Train model locally

```bash
python -m trainer.task.py
```

Check that :
- 2 new files appeared, the file downloaded from Storage and the model  
- You can now check on Google Cloud Storage that you model has been uploaded  

```bash
gsutils ls gs://$BUCKET_NAME
```

## Train model on GCP

Visit [https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training)

Inspect Makefile, complete environement variables and run
```bash
make gcp_submit_training
```

## Link the training with a new version of the model

- go to https://console.cloud.google.com/ai-platform/models
- go to taxi_fare_prediction_model
- create a new version and attach the training file (model.joblib) that you just trained.  
***`Beware here to specify skickit-learn version as 0.20.2`***