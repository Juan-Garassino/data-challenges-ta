PROJECT_ID=[YOUR_PROJECT_ID]
BUCKET_NAME=wagon-ml
REGION=europe-west1
TRAIN_FILENAME=taxi_trips_train_sample_set.csv
TEST_FILENAME=taxi_trips_test_set.csv

set_project:
	-@gcloud config set project ${PROJECT_ID}

create_bucket:
	-@gsutil mb -l ${REGION} -p ${PROJECT_ID} gs://${BUCKET_NAME}

upload_data:
	-@gsutil cp gs://wagon-ml-05-public/data/${TRAIN_FILENAME} gs://${BUCKET_NAME}/data/${TRAIN_FILENAME}
	-@gsutil cp gs://wagon-ml-05-public/data/${TEST_FILENAME} gs://${BUCKET_NAME}/data/${TEST_FILENAME}

all: set_project create_bucket upload_data
