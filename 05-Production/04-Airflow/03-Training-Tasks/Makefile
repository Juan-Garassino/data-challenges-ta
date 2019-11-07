BUCKET_NAME=wagon-data
ENV_NAME='taxipredictor'
REGION=europe-west1
DAG_FILE=dag_training_job.py
PACKAGE_NAME=trainer

upload_dags:
	-@gcloud composer environments storage dags import \
        --environment ${ENV_NAME} --location ${REGION} \
        --source ${DAG_FILE}

update_dependencies:
	-@gcloud composer environments update ${ENV_NAME} \
		--update-pypi-packages-from-file requirements.txt \
		 --location ${REGION}

build_dep:
	-@python setup.py sdist --formats=gztar

upload_dep:
	-@gsutil cp ./dist/${PACKAGE_NAME}-1.0.tar.gz gs://${BUCKET_NAME}/trainings/code/airflow/${PACKAGE_NAME}-1.0.tar.gz

clean:
	-@rm -rf dist *.egg-info

dep_upload_clean: build_dep upload_dep clean
