PROJECT_NAME=wagon-bootcamp
PROJECT_ID=wagon-bootcamp-256316
BUCKET_NAME=wagon-data
ENV_NAME='taxipredictor'
REGION=europe-west1
DAG_FILE=read_from_storage.py

upload_dags:
	-@gcloud composer environments storage dags import \
        --environment ${ENV_NAME} --location ${REGION} \
        --source ${DAG_FILE}

update_dependencies:
	-@gcloud composer environments update ${ENV_NAME} \
		--update-pypi-packages-from-file requirements.txt \
		 --location ${REGION}

