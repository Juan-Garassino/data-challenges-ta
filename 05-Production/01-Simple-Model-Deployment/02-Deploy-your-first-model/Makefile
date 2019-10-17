PACKAGE_NAME=taxi_fare
FILENAME=first_model
BUCKET_ID=iotcore-example-mlengine
JOB_NAME=taxi_fare_training_$(shell date +'%Y%m%d_%H%M%S')
REGION=europe-west1
PYTHON_VERSION=3.5
RUNTIME_VERSION=1.14
FRAMEWORK=scikit-learn
MODEL_NAME=FarePrediction

#----------------------------------
# GCP Commands
#----------------------------------

create_bucket:
	-@ROJECT_ID=$(gcloud config list project --format "value(core.project)")
	-@BUCKET_NAME=${PROJECT_ID}-mlengine
	-@echo $BUCKET_NAME

gcp_train_local:
	-@gcloud ai-platform local train \
        --package-path ${PACKAGE_NAME} \
        --module-name ${PACKAGE_NAME}.${FILENAME}

gcp_submit_training: create_package
	-@gcloud ai-platform jobs submit training ${JOB_NAME} \
        --job-dir gs://${BUCKET_ID}/scikit_learn_job_dir \
        --package-path ${PACKAGE_NAME}\
        --module-name ${PACKAGE_NAME}.${FILENAME} \
        --region ${REGION} \
        --python-version=${PYTHON_VERSION} \
        --runtime-version=${RUNTIME_VERSION}
#        --staging-bucket gs://${BUCKET_ID} \


create_gcp_model:
	-@gcloud ai-platform models create ${MODEL_NAME} \
		--regions ${REGION}
	-@gcloud ai-platform versions create baseline \
        --model ${MODEL_NAME} \
        --origin gs://${BUCKET_ID}/TaxiFare_20191016_163821 \
        --framework ${FRAMEWORK} \
        --python-version=${PYTHON_VERSION} \
        --runtime-version=${RUNTIME_VERSION}

eval_gcp_local:
#	-@gcloud ai-platform local predict --model-dir gs://${BUCKET_ID}/TaxiFare_20191016_163821
	-@gcloud ai-platform local predict --model-dir model/ \
        --json-instances ../data/test.json \
        --framework scikit-learn

eval_gcp_online:
#	-@gcloud ai-platform local predict --model-dir gs://${BUCKET_ID}/TaxiFare_20191016_133849
	-@gcloud ai-platform predict --model ${MODEL_NAME} \
        --text-instances ../data/test_100.txt \
        --version baseline
#----------------------------------
# LOCAL COMMANDS
#----------------------------------

create_package:
	-@mkdir ${PACKAGE_NAME}
	-@touch ${PACKAGE_NAME}/__init__.py
	-@cp ${FILENAME}.py ${PACKAGE_NAME}

train_simple_model:
	-@python first_model.py

clean:
	-@rm *.csv *.joblib
	-@echo ${JOB_NAME}

test_local:
	-@python test.py

