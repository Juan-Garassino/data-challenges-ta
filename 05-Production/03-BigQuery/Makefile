PROJECT_NAME=wagon-bootcamp
PROJECT_ID=wagon-bootcamp-256316
BUCKET_NAME=wagon-data
REGION=europe-west1

unzip:
	-@gunzip ../data/${FILENAME}.gz

download_kaggle_data:
	-@pip install kaggle
	-@kaggle competitions download -c new-york-city-taxi-fare-prediction

upload_data:
	-@gsutil cp ~/Downloads/new-york-city-taxi-fare-prediction/train.csv gs://${BUCKET_NAME}/train.csv



