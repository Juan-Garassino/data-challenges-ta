ENV_NAME='taxipredictor'
REGION=europe-west1
DAG_FILE=dag_enriching.py
PACKAGE_NAME=trainer

upload_dags:
	-@gcloud composer environments storage dags import \
        --environment ${ENV_NAME} --location ${REGION} \
        --source ${DAG_FILE}
	-@gcloud composer environments storage dags import \
        --environment ${ENV_NAME} --location ${REGION} \
        --source api_insert.py
