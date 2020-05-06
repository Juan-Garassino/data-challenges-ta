# Objective

Let's create a model version on GCP that we'll be able to call later on from the command line to do some prediction.

## First install correct dependencies 

In order to be aligned with AI platform 1.15 runtine (just run following command for now you'll understand why later in the exercise)

```bash
pip install -r requirements.txt
```
Check that dependencies inside requirements.txt are the same as in setup.py file

## Create a model

Go to [AI Platformn](https://console.cloud.google.com/ai-platform/models) and create a model

## Create a version

Each model has different versions deployed. Create now your first version  

On [AI Platformn model page](https://console.cloud.google.com/ai-platform/models) your first version of the model.

Here's a quick guide for the form:

- Python version `3.7` (same as training job)
- Framework : `scikit-learn`
- Framework version: `0.20.4` (should ring a bell => `requirements.txt` and `steup.py`)
- ML runtime version: `1.15` 
- Cloud Storage path where you uploaded the model file. :warning: Select the **Folder**, not the `model.joblib` file...

## Create a Makefile command

**Here we might want to create a makefile command in order to be able to call the full deployment process in one global makefile command, instead of using the web UI**

In order to be able to create version from gcloud cli, you need to update beta version of `gcloud` :   

```bash
gcloud components install beta
```

Add to `Makefile` a `create_version` command:

```bash
# Makefile
# [...]

create_version:
	gcloud beta ai-platform versions create ${VERSION_NAME} \
		--model ${MODEL_NAME} \
		--origin gs://${BUCKET_NAME}/models/taxi_fare_model/versionLivecode \
		--python-version ${PYTHON_VERSION} \
		--runtime-version ${RUNTIME_VERSION} \
		--framework=${FRAMEWORK}
```

Check that you correctly defined `MODEL_NAME`, `VERSION_NAME`, `PATH_TO_MODEL`, `PYTHON_VERSION`, `RUNTIME_VERSION` at the top of the `Makefile`.

Now to test the whole deployment process you will:

- Submit a new training job, i.e a new `model.joblib`
- Create a new version attached to that new `model.joblib`

To do that:

1. Change `VERSION_NAME` to a new name, `v1` for instance
2. Set `MODEL_VERSION` inside `trainer.py` with a new name
3. Set `PATH_TO_MODEL` inside Makefile (corresponding to `MODEL_VERSION` above inside Makefile)
4. Run the following commands:

```bash
make gcp_submit_training
make create_version
``` 
**NB: When you create a version, GCP will try to load the model with the version of scikit-learn of the [1.15 runtime version](https://cloud.google.com/ai-platform/training/docs/runtime-version-list)**
So make sure that you have submited your training with the dependencies from runtime 1.15:
```bash
pandas==0.24.2
scipy==1.2.2
scikit-learn==0.20.4
```
If not install the dependencies above and run again (delete your version first:
```bash
make gcp_submit_training
make create_version
``` 
