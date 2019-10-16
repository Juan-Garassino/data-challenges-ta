## Objective

Train first model on GCP  
The aim here is to focus on the whole pipeline, implement few preprocessing

## Create Bucket

Start by defining a project name
```bash
PROJECT_ID=$(gcloud config list project --format "value(core.project)")
BUCKET_NAME=${PROJECT_ID}-mlengine
echo $BUCKET_NAME
```

Then create bucket
BEWARE HERE chose adapted region 
```bash
REGION=europe-west1
gsutil mb -l $REGION gs://$BUCKET_NAME
```

## Install correct requirements for this challenge

```bash
pip install -r requirements.txt
```

## Complete fisrt_model.py

Open it and complete to train first model on GCloud as seen this morning  
No preporcessing here

## Train locally

```bash
python first_model.py
```

Check that :
- 2 new files appeared, the file downloaded from Storage and the model  
- You can now check on Google Cloud Storage that you model has been uploaded  

```bash
gsutils ls gs://[BUCKET_NAME]/
```

## Test Locally 

Inspect Makefile and run  
```bash
make test_local
```

A score should appear on the model you trained  

Now clean your package
```bash
make clean
```

## Train Model on GCP

Inspect Makefile, complete environement variables and run
```bash
make gcp_submit_training
```

## Deploy model on GCP

```bash
gcloud ai-platform models create "[YOUR-MODEL-NAME]"
```

