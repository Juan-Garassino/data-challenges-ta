ENV_NAME='XXXXXXXXX'
REGION=europe-west1


update_dependencies:
	-@gcloud composer environments update ${ENV_NAME} \
		--update-pypi-packages-from-file requirements.txt \
		 --location ${REGION}

