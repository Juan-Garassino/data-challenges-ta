PACKAGE_NAME=XXX
FILENAME=XXX
BUCKET_NAME=wagon-ml-models
PROJECT_ID=XXX
JOB_NAME=taxi_fare_model_$(shell date +'%Y%m%d_%H%M%S')
REGION=europe-west1
PYTHON_VERSION=3.5
RUNTIME_VERSION=1.13
FRAMEWORK=scikit-learn
MODEL_NAME=taxi_fare_prediction_model

create_bucket:
	-@gsutil mb -l ${REGION} -p ${PROJECT_ID} gs://${BUCKET_NAME}

gcp_submit_training:
	gcloud ai-platform jobs submit training ${JOB_NAME} \
		--job-dir gs://${BUCKET_NAME}/trainings  \
		--package-path ${PACKAGE_NAME} \
		--module-name ${PACKAGE_NAME}.${FILENAME} \
		--python-version=${PYTHON_VERSION} \
		--runtime-version=${RUNTIME_VERSION} \
		--region ${REGION}

run_locally:
	-@python -m ${PACKAGE_NAME}.${FILENAME}


