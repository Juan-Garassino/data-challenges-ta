ENV_NAME=TODO
BUCKET_NAME=TODO
DAG_FILE=TODO

PACKAGE_NAME=TaxiFareModel
FILENAME=trainer
REGION=europe-west1

run_locally:
	@python -m ${PACKAGE_NAME}.${FILENAME}

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

all: build_dep upload_dep upload_dags clean

# ----------------------------------
#    CLEANING COMMANDS
# ----------------------------------

clean:
	@rm -fr */__pycache__
	@rm -fr __init__.py
	@rm -fr build
	@rm -fr dist
	@rm -fr ${PACKAGE_NAME}-*.dist-info
	@rm -fr ${PACKAGE_NAME}.egg-info
