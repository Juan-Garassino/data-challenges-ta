# Objective

Now, your will train your first model on GCP.
The goal is to build a very simple model for the taxi fare prediction problem. The focus is to build a deployment pipeline that will be easy to iterate on and improve. We will not try to make the model accurate yet. We will make improvements later.

## Install dependencies

```bash
    pip install -r requirements.txt
```

## Create a Model

- go to https://console.cloud.google.com/ai-platform/models
- create a model `taxi_fare_prediction_model`

## Complete task.py

Open it and complete to train your first model on GCloud as seen in the course.

## Train model locally

```bash
python -m trainer.task
```

Check that :
- model.joblib file was stored locally
- You can now check on Google Cloud Storage that you model has been uploaded  

```bash
gsutil ls gs://[YOUR_BUCKET_NAME]
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
