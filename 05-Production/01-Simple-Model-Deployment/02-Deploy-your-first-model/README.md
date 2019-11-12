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

Open it and complete to train your first model on GCloud as seen in the course: 
- Complete `get_data()` 
- Chose your model inside `train_model()`
- Complete `preprocess()` 
- Complete main section at the end
- complete setup.py file if needed, specifically the requirements.txt

**_NB: depending on the library you'll use, you might want to specify the exact version inside setup.py, so that when you train your model on GCP or locally you have the same requirements_**

## Train model locally
First make sure you have the same dependencies inside you `requirements.txt `and inside `setup.py`  
**_Reminder : You will train locally (execute task.py locally) an then train it on GCP (execute task.py on GCP)  
==> Making sure your dependencies match ensures you script to run identically both locally and on GCP_**

Now train locally:
```bash
pip isntall -r requirements.txt
python -m trainer.task
```

Check that :
- your model `model.joblib` has been stored locally
- your model `model.joblib` has been stored on your cloud Storage Bucket

```bash
gsutil ls gs://[YOUR_BUCKET_NAME]/models/taxi_fare_model
```

## Train model on GCP

You will now train your model on GCP, meaning executing task.py on a GCP server instead of locally  

Visit doc on [gcloud ai-platform jobs submit training](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training) cli command  
Inspect Makefile, complete environement variables, **_make sure to understand every argument inside `gcp_submit_training` command_**, then run it:
```bash
make gcp_submit_training
```
Visualize you job inside AI Platform  
Launch another time `make gcp_sumbit_training`:
- How many jobs do you see on the console ? 
- How many model.joblib files were stored, and where ?
- What might you want to change here ?


## Create a version 
Here Creating a version 

- go to https://console.cloud.google.com/ai-platform/models
- go to taxi_fare_prediction_model
- create a new version indicating Bucket location of the model model.joblib you just stored on a Bucket (when executing task.py)
***`Beware here to specify skickit-learn version as 0.20.2`***


## Recap
Now take a step back, what have you done exactly while:
- running `make gcp_submit_trainig` ?
- creating a version ?  

_**What is the final goal of deploying a model ?**_   

**_Therefore what is according to you the point in creating a version ?_**  

**_Why would we want to create a version ? We already have the trained model stored somewhere in the cloud, isn't that enough ?_**   


## To go further, Makefile power

Imagine you have to repeat that workflow every time you create a new model.  

You might want to automatize the process right (specifically the version creation)?  

Implement following make command inside your Makefile:
- `create_model`
- `create_version`
- `delete version`
- `delete_model`
- `all`

What would you want `make all` to do exactly
