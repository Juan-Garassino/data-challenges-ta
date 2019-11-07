## Objective

Create Workflow launching Training Tasks everyday

Here we will train our model on enriched Data with weather.

We'll start from yesterday's last exercice. You can see below the target architecture for our project. For now, we will focus on building the historical training table, and schedule the training session in our DAG. We will work in the incremental update and custom class later.

![Updated diagram](https://i.imgur.com/zMuCeqc.png)

## Create new table containing weather and raw data

Create `train_weather_ny_history` Table, in EU region, by uploading `NY_weather_data.csv` file.

Then create a Table merging original data with weather data.  
To do that run from BQ Query editor the command:
```bash
select
  TT.*,
  NY.TMAX,
  NY.TMIN,
  NY.SNWD
from `artful-willow-239109.GMBInput.taxi_trips`        AS TT
LEFT JOIN `artful-willow-239109.GMBInput.NY_Weather_Data` AS NY
ON CAST(TT.pickup_datetime AS Date) = CAST(NY.DATE AS Date)
``` 

Save results from that command into you new Table.

This table will be your new training set.

## Prerequisites


Now that we've submitted dozens of training jobs from Makefiles commands, we all agree that running make commands is boring, we'd rather have someone else submitting the training jobs for us, Airflow is our man. 

Before carrying on, make sure you are clear with following concepts:  

- utility of `setup.py` when submiting training job
- `a training job submission` **is equivalent to** `running task.py file (therefore to training our model) on GCP AND uploading model.joblib to Storage bucket`


## Launch Training Task

Here We go back from yesterday's trainer package:
- we only train on **_last 1000000 rows_**
- we don't forget the `setup.py` specifying packages and correct python requirements 
- we name our model directory `airflow_v1`, so that we'll overwrite model every day

Here we just worry about training, **_no version creation for the moment_**

Inspect the Makefile, and notice that tere is no `gcp_submit_training` command.

Simply because we'll do that from Airflow now:
- read documentation for [MLEngineTrainingOperator](https://airflow.apache.org/_api/airflow/contrib/operators/mlengine_operator/index.html#airflow.contrib.operators.mlengine_operator.MLEngineTrainingOperator), does any of the parameters look familiar to you ?  
- open `dag_training_job.py`, and fill in variables just like Makefile from yesterday
- what should you specify in `package_uris` variable ? 
- you might wonder why we need `package_uris` now ? Answer on this [slackoverflow post](https://stackoverflow.com/questions/54401965/airflow-ml-engine-package-uri)


To update DAG to Airflow, build dependencies first (ask TA or T if not clear):

```bash
make build_dep upload_dep
``` 
Then upload your DAG:

```bash
make upload_dag 
``` 



