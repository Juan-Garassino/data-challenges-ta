PACKAGE_NAME=trainer
FILENAME=task
BUCKET_NAME=wagon-ml-trainings
PROJECT_ID=wagon-bootcamp-256316
JOB_NAME=taxi_fare_training_$(shell date +'%Y%m%d_%H%M%S')
REGION=europe-west1
PYTHON_VERSION=3.5
RUNTIME_VERSION=1.13
FRAMEWORK=scikit-learn
MODEL_NAME=taxi_fare_prediction_model
CREDENTIALS=/Users/jeanbizot/google-credentials/wagon-bootcamp-3567d0ae8e1e.json
#----------------------------------
# GCP Commands
#----------------------------------

create_bucket:
	-@gsutil mb -l ${REGION} -p ${PROJECT_ID} gs://${BUCKET_NAME}

gcp_train_local:
	-@gcloud ai-platform local train \
        --package-path ${PACKAGE_NAME} \
        --module-name ${PACKAGE_NAME}.${FILENAME}

gcp_submit_training:
	gcloud ai-platform jobs submit training ${JOB_NAME} \
		--job-dir gs://${BUCKET_NAME}/trainings  \
		--package-path ${PACKAGE_NAME} \
		--module-name ${PACKAGE_NAME}.${FILENAME} \
		--python-version=${PYTHON_VERSION} \
		--runtime-version=${RUNTIME_VERSION} \
		--region ${REGION}

create_gcp_model:
	-@gcloud ai-platform models create ${MODEL_NAME} \
		--regions ${REGION}
	-@gcloud ai-platform versions create baseline \
		 --model ${MODEL_NAME} \
		 --origin gs://wagon-data/TaxiFare_20191023_181342 \
		 --framework ${FRAMEWORK} \
		 --python-version=${PYTHON_VERSION} \
		 --runtime-version=${RUNTIME_VERSION}
#----------------------------------
# LOCAL COMMANDS
#----------------------------------

#create_package:
#	-@mkdir ${PACKAGE_NAME}
#	-@touch ${PACKAGE_NAME}/__init__.py
#	-@cp ${FILENAME}.py ${PACKAGE_NAME}

train_simple_model:
	-@python -m ${PACKAGE_NAME}.${FILENAME}

clean:
	-@rm ${PACKAGE_NAME}/*.csv ${PACKAGE_NAME}/*.joblib
	-@echo ${JOB_NAME}



