## Objective

Create Workflow launching Training Tasks everyday

Here we will train our model on enriched Data with weather.

We'll start from yesterday's last exercice. 

## Create new table containing weather and raw data

Create `train_weather_ny_history` Table, in EU region, by uploading `NY_weather_data.csv` file.

Then create a Table merging original data with weather data.  
To do that select the dataset you created run from BQ Query editor the command:
```sql
create table taxiFareWeather;
select
  TT.*,
  NY.TMAX,
  NY.TMIN,
  NY.SNWD
from  `your-projectid.dataset.traintable` as TT
left join `your-projectid.dataset.weatherdata` as NY
ON CAST(TT.pickup_datetime AS Date) = CAST(NY.DATE as Date)
``` 

Save results from that command into you new Table.

This table will be your new training set.  

**NB**: Your new training table is slighty different from your train.csv file:
- field `key` has been replaced by `trip_key`
- new column `test` has been added to be able to filter training from test set

## Prerequisites

Now that we've submitted dozens of training jobs from Makefiles commands, we all agree that running make commands is boring, we'd rather have someone else submitting the training jobs for us, Airflow is our man. 

Before carrying on, make sure you are clear with following concepts:  

- utility of `setup.py` when submiting training job
- `a training job submission` **is equivalent to** `running trainer.py file (therefore to training our model) on GCP AND uploading model.joblib to a Storage bucket`


## Launch Training Task

Here We go back from yesterday's TaxiFareModel package and change a few things:
- Change `get_data()` function to `get_data_from_bq()` you implemented in last exercice. 
- we'll only train on **_last 1000000 rows_**
- don't forget the `setup.py` specifying packages and correct python requirements (we added google-cloud-bigquery for you) 
- name your model directory `airflow_v1`, so that we'll overwrite model every day

Here we just worry about training, **_no version creation for the moment_**

Inspect the Makefile, and notice that there is no `gcp_submit_training` command

Simply because we'll do that from Airflow now, we will use an Operator that will run the equivalent of our `make gcp_submit_traing`:
- read documentation for [MLEngineTrainingOperator](https://airflow.apache.org/_api/airflow/contrib/operators/mlengine_operator/index.html#airflow.contrib.operators.mlengine_operator.MLEngineTrainingOperator), does any of the parameters look familiar to you ?  
- open `dag_training_job.py`, and fill in variables just like Makefile from yesterday
- you might wonder why we need `package_uris` now ? Answer on this [slackoverflow post](https://stackoverflow.com/questions/54401965/airflow-ml-engine-package-uri)
- get function get_data_from_bg() from last exercice and insert it into `data.py`
- **IMPORTANT** test your `trainer.py` before trying to update your dag to airflow:
```bash
make run_locally
``` 
- Inspect different machines to run on [HERE](https://cloud.google.com/ai-platform/training/docs/machine-types) and change the machine type if you wish.


To update DAG to Airflow, build dependencies first (ask TA or T if not clear):

```bash
make build_dep upload_dep
``` 
Then upload your DAG:

```bash
make upload_dag 
``` 

## RECAP

You have now a DAG on airflow that triggers training tasks every day  
That training task saves a model to your BUCKET storage  

Concerning the version creation, you have 2 choices:
- Either use an already existing version pointing at your storage bucket from training tasks launched by airflow
- Eihter create one manually form GCP interface (No need to automate here, we only want to troger new **trainings** every day)

