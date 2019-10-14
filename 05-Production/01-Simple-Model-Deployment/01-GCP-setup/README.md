## Objective

Set up yout GCP account and install first sdk

## Create GCP project

Connect to your IKEA-GCP account and create a project
use wagon-bootcamp as project name
https://console.cloud.google.com/cloud-resource-manager


## Install GCP sdk

Simply follow
https://cloud.google.com/sdk/

## Test installation

Upload csv file into Google Cloud Storage
Open Makefile
```bash
make create_bucket unzip upload_data
```
