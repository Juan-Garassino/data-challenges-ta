# Objective

Set up yout GCP account and install first sdk

## Create GCP project

 - Connect to your IKEA-GCP account and create a project
 - Use **_wagon-bootcamp_** as project name
https://console.cloud.google.com/cloud-resource-manager


## Create Service Account key
Go to [Service Account key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey?hl=fr&_ga=2.45500263.-2144345341.1571415069)  
Create a new Service Account key and set Role as `project owner`  
Download json, and store it somewhere you'll remeber on your laptop  
Then append `export GOOGLE_APPLICATION_CREDENTIALS="PATH_TO_KEY"` to `.zshrc` file by running : 


    echo "export GOOGLE_APPLICATION_CREDENTIALS="PATH_TO_KEY"" >> ~/.zshrc

## Install GCP sdk

Simply follow
https://cloud.google.com/sdk/docs/quickstarts

## Create a Google Cloud Storage Bucket

For most of this week challenges, you will need a Google Cloud Storage bucket. 

- Chose a **_unique_** bucket name, i.e `wagon-ml-[YOURNAME]`
- Open Makefile, replace `BUCKET_NAME` env variable with your name
- run following command in your terminal: 


    make create_bucket

Make sure you set the right `${PROJECT_ID}` variable at the top of the Makefile.  
`PROJECT_ID` is the **_ID_** and not the **_name_**

## Upload the challenge dataset into your bucket

The data is already stored on a google cloud public bucket
- training sample data [gs://wagon-ml-05-public/data/taxi_trips_train_sample_set.csv](gs://wagon-ml-05-public/data/taxi_trips_train_sample_set.csv)
- test data [gs://wagon-ml-05-public/data/taxi_trips_test_set.csv](gs://wagon-ml-05-public/data/taxi_trips_test_set.csv)

To upload this data into your bucket, run the Makefile command:

```
make upload_data
```

The training dataset should now be visible into your `wagon-ml/data` folder.
Go to [Storage tab](https://console.cloud.google.com/storage) and make sure that both datasets are now be visible in your bucket inside folder `/data`

## Troubleshooting

### AccessDeniedException: 403 The project to be billed is associated with an absent billing account.

- Make sure that billing is enabled for your Google Cloud Platform project.
https://cloud.google.com/billing/docs/how-to/modify-project
- Make sure you set the right project_id in the Makefile

