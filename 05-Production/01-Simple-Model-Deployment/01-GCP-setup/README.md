# Objective

Set up yout GCP account and install first sdk

## Create GCP project

 - Connect to your IKEA-GCP account and create a project
 - Use wagon-bootcamp as project name
https://console.cloud.google.com/cloud-resource-manager


## Install GCP sdk

Simply follow
https://cloud.google.com/sdk/

## Create a Google Cloud Storage Bucket

For most of this week challenges, you will need a Google Cloud Storage bucket. 

- Create a bucket named `wagon-ml` by running the Makefile command within a terminal 

```
make create_bucket
```

Make sure you set the right `${PROJECT_ID}` variable at the top of the Makefile.

## Upload the challenge dataset into your bucket

The data is already stored on a google cloud public bucket
- training sample data [gs://wagon-ml-05-public/data/taxi_trips_train_sample_set.csv](gs://wagon-ml-05-public/data/taxi_trips_train_sample_set.csv)
- test data [gs://wagon-ml-05-public/data/taxi_trips_test_set.csv](gs://wagon-ml-05-public/data/taxi_trips_test_set.csv)

To upload this data into your bucket, run the Makefile command:

```
make upload_data
```

The training dataset should now be visible into your `wagon-ml/data` folder.
Go to https://console.cloud.google.com/storage and make sure the training dataset is now be visible in your bucket inside folder `/data`

## Troubleshooting

### AccessDeniedException: 403 The project to be billed is associated with an absent billing account.

- Make sure that billing is enabled for your Google Cloud Platform project.
https://cloud.google.com/billing/docs/how-to/modify-project
- Make sure you set the right project_id in the Makefile

