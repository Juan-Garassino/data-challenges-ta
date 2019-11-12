# Objective

Set up yout GCP account and install first sdk

## Create GCP project

 - Connect to your GCP account and create a project
 - Use **_wagon-bootcamp_** as project name
https://console.cloud.google.com/cloud-resource-manager


## Create Service Account key
Go to [Service Account key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey) 
Create a new Service Account key :
- set Role as `project > owner`
- Set the service account name `data-challenges`   
Download json, and store it under `~/gcp_credentials.json`

Then append `export GOOGLE_APPLICATION_CREDENTIALS="~/gcp_credentials.json"` to `.zshrc` file by running : 
```bash
echo "export GOOGLE_APPLICATION_CREDENTIALS="~/gcp_credentials.json"" >> ~/.zshrc
```
### Troubleshooting

`AccessDeniedException: 403 The project to be billed is associated with an absent billing account.`

- Make sure that billing is enabled for your Google Cloud Platform project.
https://cloud.google.com/billing/docs/how-to/modify-project
- Make sure you set the right project_id in the Makefile

## Install GCP sdk

Simply follow https://cloud.google.com/sdk/docs/quickstarts
Help on MacOS:  
- Don't forget to run `./google-cloud-sdk/install.sh` command if needed, read instructions carefully when asked [Y/n] answers
 

## Create a Google Cloud Storage Bucket

For most of this week challenges, you will need a Google Cloud Storage bucket. 

- Chose a **_unique_** bucket name, i.e `wagon-ml-[YOURNAME]`
- Open Makefile, replace `BUCKET_NAME` env variable with your name
- run following command in your terminal: 
```bash
make create_bucket
```

Make sure you set the right `PROJECT_ID` and `BUCKET_NAME` variable at the top of the Makefile.  
`PROJECT_ID` is the **_ID_** and not the **_name_**

## Upload the challenge dataset into your bucket

The data is already stored on a google cloud public bucket
- training sample data [gs://wagon-ml-05-public/data/taxi_trips_train_sample_set.csv](gs://wagon-ml-05-public/data/taxi_trips_train_sample_set.csv)
- test data [gs://wagon-ml-05-public/data/taxi_trips_test_set.csv](gs://wagon-ml-05-public/data/taxi_trips_test_set.csv)

To upload this data into your bucket, run the Makefile command:

```bash
make upload_data
```

The training dataset should now be visible into your `wagon-ml/data` folder.
Go to [Storage tab](https://console.cloud.google.com/storage) and make sure that both datasets are now be visible in your bucket inside folder `/data`

## Python Setup 

Install virtualenv:

```bash
conda install virtualenv
```
Create your virtualenv
    
```bash
cd ~/
virtualenv -p python3 venv3
```

Activate your virtualenv
```bash
source ~/venv3/bin/activate
```

You should now be in your venv3 and see `(venv3)` your shell:

```bash
(venv3) jeanbizot@MacBook-Pro-5:~$ cd ~/
```
Install ipython and jupyter notebook:
 
```bash
pip install ipython jupyter 
```
Make virtualenv activation persistent by adding it to your `.zshrc`  

**_NB : every time you open a new terminal, `source .zshrc `is being computed_**

For MACOS:
```bash
echo "source ~/venv3/bin/activate" >> ~/.zshrc
```
    
For Windows:
```bash
echo "source ~/venv3/Scripts/activate" >> ~/.zshrc
```

Now every time you'll open a terminal window you'll be inside your python3 virtual environnement
