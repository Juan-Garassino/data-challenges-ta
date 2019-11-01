# Objective

Set up yout GCP account and install first sdk

## Create GCP project

 - Connect to your IKEA-GCP account and create a project
 - Use wagon-bootcamp as project name
https://console.cloud.google.com/cloud-resource-manager


## Install GCP sdk

Simply follow
https://cloud.google.com/sdk/

## Upload data into your own bucket

The data is already stored on a google cloud bucket
- training sample data [gs://wagon-ml-05-public/data/taxi_trips_train_sample_set.csv](gs://wagon-ml-05-public/data/taxi_trips_train_sample_set.csv)
- test data [gs://wagon-ml-05-public/data/taxi_trips_test_set.csv](gs://wagon-ml-05-public/data/taxi_trips_test_set.csv)

To upload this data into your own bucket, run the Makefile by setting the right variables at the top of the file.

Then run it within a console:
```
make all
```

Then go to https://console.cloud.google.com/storage and make sure the data has correcly been uploaded in your bucket.

## Troubleshooting

### AccessDeniedException: 403 The project to be billed is associated with an absent billing account.

- Make sure that billing is enabled for your Google Cloud Platform project.
https://cloud.google.com/billing/docs/how-to/modify-project
- Make sure you set the right project_id in the Makefile

