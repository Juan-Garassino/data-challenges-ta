PROJECT_NAME=wagon-bootcamp
PROJECT_ID=wagon-bootcamp-256007
BUCKET_NAME=wagon-ml-data
REGION=europe-west1

set_project:
	-@gcloud config set project ${PROJECT_ID}

unzip:
	-@gunzip ../data/${FILENAME}.gz

create_bucket:
	-@gsutil mb -l ${REGION} -p ${PROJECT_ID} gs://${BUCKET_NAME}/

delete_bucket:
	-@gsutil rm -r gs://${BUCKET_NAME}

upload_data:
	-@gsutil cp ../data/05_Production_TaxiFare_100000.csv gs://${BUCKET_NAME}/05_Production_TaxiFare_100000.csv

all: set_project create_bucket unzip upload_data
