AIRFLOW_INSTANCE_NAME=TODO
REGION=europe-west1

upload_dags:
	-@gcloud composer environments storage dags import \
        --environment ${AIRFLOW_INSTANCE_NAME} --location ${REGION} \
        --source first_dag.py

update_dependencies:
	-@gcloud composer environments update ${AIRFLOW_INSTANCE_NAME} \
		--update-pypi-packages-from-file requirements.txt \
		 --location ${REGION}
