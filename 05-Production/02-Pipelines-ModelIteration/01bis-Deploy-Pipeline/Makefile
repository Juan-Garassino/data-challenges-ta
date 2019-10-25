PACKAGE_NAME=trainer
FILENAME=train
BUCKET_NAME=wagon-ml-trainings
PROJECT_ID=wagon-bootcamp-256316
JOB_NAME=taxi_fare_training_pipeline_$(shell date +'%Y%m%d_%H%M%S')
REGION=europe-west1
PYTHON_VERSION=3.5
RUNTIME_VERSION=1.13
FRAMEWORK=scikit-learn
MODEL_NAME=taxi_fare_prediction_model
CREDENTIALS=/Users/jeanbizot/google-credentials/wagon-bootcamp-3567d0ae8e1e.json

#----------------------------------
# LOCAL COMMANDS
#----------------------------------

create_package:
	-@mkdir ${PACKAGE_NAME}
	-@touch ${PACKAGE_NAME}/__init__.py
	-@touch ${PACKAGE_NAME}/pipeline.py
	-@touch ${PACKAGE_NAME}/tools.py

train_simple_model:
	-@python -m ${PACKAGE_NAME}.${FILENAME}

gcp_submit_training:
	gcloud ai-platform jobs submit training ${JOB_NAME} \
		--job-dir gs://${BUCKET_NAME}/trainings  \
		--package-path ${PACKAGE_NAME} \
		--module-name ${PACKAGE_NAME}.${FILENAME} \
		--python-version=${PYTHON_VERSION} \
		--runtime-version=${RUNTIME_VERSION} \
		--stream-logs \
		--region ${REGION}

clean:
	-@rm *.csv *.joblib

build_dep:
	-@python setup.py sdist --formats=gztar

upload_dep:
	-@gsutil cp ./dist/${PACKAGE_NAME}-1.0.tar.gz gs://${BUCKET_NAME}/trainings/code/${PACKAGE_NAME}-1.0.tar.gz

create_version_pipeline:
	-@gcloud components install beta
	-@gcloud beta ai-platform versions create pipeline_v0 \
		--model ${MODEL_NAME} \
		--origin gs://wagon-data/TaxiFare_pipeline_20191024_115902 \
		--framework ${FRAMEWORK} \
		--python-version=${PYTHON_VERSION} \
		--runtime-version=${RUNTIME_VERSION} \
        --package-uris gs://${BUCKET_NAME}/trainings/code/${PACKAGE_NAME}-1.0.tar.gz

