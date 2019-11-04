PACKAGE_NAME=XXXXX
FILENAME=XXXX
BUCKET_NAME=XXXXX
PROJECT_ID=XXXXX
JOB_NAME=taxi_fare_training_pipeline_$(shell date +'%Y%m%d_%H%M%S')
REGION=europe-west1
PYTHON_VERSION=3.5
RUNTIME_VERSION=1.14
FRAMEWORK=scikit-learn
MODEL_NAME=taxi_fare_prediction_model

VERSION_NAME=XXXXXX

gcp_submit_training:
	-@gcloud ai-platform jobs submit training ${JOB_NAME} \
		--job-dir gs://${BUCKET_NAME}/trainings  \
		--package-path ${PACKAGE_NAME} \
		--module-name ${PACKAGE_NAME}.${FILENAME} \
		--python-version=${PYTHON_VERSION} \
		--runtime-version=${RUNTIME_VERSION} \
		--region ${REGION} \
		--stream-logs

build_dep:
	-@python setup.py sdist --formats=gztar

upload_dep:
	-@gsutil cp ./dist/${PACKAGE_NAME}-1.0.tar.gz gs://${BUCKET_NAME}/trainings/code/${PACKAGE_NAME}-1.0.tar.gz

create_pipeline_version:
	-@gcloud components install beta
	-@gcloud beta ai-platform versions create ${VERSION_NAME} \
		--model ${MODEL_NAME} \
		--origin gs://wagon-ml/models/taxi_fare_model/pipeline_v1 \
		--python-version ${PYTHON_VERSION} \
		--runtime-version ${RUNTIME_VERSION} \
		--prediction-class predictor.Predictor \
    	--package-uris gs://${BUCKET_NAME}/trainings/code/${PACKAGE_NAME}-1.0.tar.gz

all:
	gcp_submit_training build_dep upload_dep create_pipeline_version