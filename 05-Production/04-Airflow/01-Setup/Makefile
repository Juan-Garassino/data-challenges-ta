PROJECT_NAME=wagon-bootcamp
PROJECT_ID=wagon-bootcamp-256316
BUCKET_NAME=wagon-data
ENV_NAME='taxipredictor'
REGION=europe-west1

upload_dags:
	-@gcloud composer environments storage dags import \
        --environment ${ENV_NAME} --location ${REGION} \
        --source first_dag.py

