# Objective

Finish the Deployment process, you've submited training jobs, now let us create a version that we'll be able to call later on.

## Create a model

Before you can use your model, you need to create a model resource on AI Platform and link a version to the model file.
- Go to [AI Platformn](https://console.cloud.google.com/ai-platform/models) and create a model


## Create a version

Each model has different versions deployed. Create now your first version  

On [AI Platformn model page](https://console.cloud.google.com/ai-platform/models) your first version of the model  
For that make sure to specify: 
- Python version `3.7` (same as training job)
- Framework : `scikit-learn`
- Framework version: `0.20.4`
- ML runtime version: `1.15` 
- Cloud Storage path where you uploaded the model file
     NB: Browse the **Folder**, not the `model.joblib`

## Create a Makefile command

**Here we might want to create a makefile command in order to be able to call the full deployment process in one global makefile commad**

In order to be able to create version from gcloud cli, you need to update beta version of `gcloud`    
```bash
gcloud components install beta
```

Add to Makefile a `create_version` command:
```bash
create_pipeline_version:
	gcloud beta ai-platform versions create ${VERSION_NAME} \
		--model ${MODEL_NAME} \
		--origin gs://${BUCKET_NAME}/models/taxi_fare_model/versionLivecode \
		--python-version ${PYTHON_VERSION} \
		--runtime-version ${RUNTIME_VERSION} \
		--framework=${FRAMEWORK}
```
Check that you correctly defined `MODEL_NAME`, `VERSION_NAME`, `PATH_TO_MODEL`, `PYTHON_VERSION`, `RUNTIME_VERSION`

Now to test the whole deployment process you will :
- submit a new training job, i.e a new `model.joblib`
- create a new version attached to that new `model.joblib`

To do that:
- edit `MODEL_VERSION` inside trainer.py with a new name
- edit `PATH_TO_MODEL` inside Makefile (corresponding to `MODEL_VERSION` above inside Makefile)
- run :
```bash
make gcp_submit_training
make create_version
``` 