ENV_NAME='XXXXXX'
REGION=europe-west1

upload_dags:
	-@gcloud composer environments storage dags import \
        --environment ${ENV_NAME} --location ${REGION} \
        --source first_dag.py

