PROJECT_NAME=wagon_bootcamp_data
PROJECT_ID=iotcore-example
BUCKET_NAME=wagon-ml-production

set_project:
	-@gcloud config set project ${PROJECT_ID}

unzip:
	-@gunzip ../data/05_Production_TaxiFare_100000.csv.gz

create_bucket:
	-@gsutil mb -p ${PROJECT_ID} gs://${BUCKET_NAME}/

upload_data:
	-@gsutil cp data/05_Production_TaxiFare_100000.csv gs://${BUCKET_NAME}/05_Production_TaxiFare_100000.csv

ls:
	-@gsutil ls

all: set_project create_bucket unzip upload_data ls
