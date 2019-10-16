## Objective

Set up yout GCP account and install first sdk

## Create GCP project

 - Connect to your IKEA-GCP account and create a project
 - Use wagon-bootcamp as project name
https://console.cloud.google.com/cloud-resource-manager


## Install GCP sdk

Simply follow
https://cloud.google.com/sdk/

## Test installation

 - Upload csv file into Google Cloud Storage
 - Open Makefile
 - Create bucket into Google Cloud Storage and load data:
```bash
make create_bucket unzip upload_data
```
Go to https://console.cloud.google.com/storage and make sure the data has correcly been uploaded in your bucket.


## Troubleshooting

### AccessDeniedException: 403 The project to be billed is associated with an absent billing account.

- Make sure that billing is enabled for your Google Cloud Platform project.
https://cloud.google.com/billing/docs/how-to/modify-project
- Make sure you set the right project_id in the Makefile

