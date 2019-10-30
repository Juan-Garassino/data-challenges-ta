PROJECT_ID=[YOUR_PROJECT_ID]
BUCKET_NAME=wagon-ml-data
REGION=europe-west1

set_project:
	-@gcloud config set project ${PROJECT_ID}

create_bucket:
	-@gsutil mb -l ${REGION} -p ${PROJECT_ID} gs://${BUCKET_NAME}

delete_bucket:
	-@gsutil rm -r gs://${BUCKET_NAME}

upload_data:
	-@gsutil cp gs://wagon-ml-05-data/taxi_trips_train_sample_set.csv gs://${BUCKET_NAME}/${FILENAME}

all: set_project create_bucket upload_data
