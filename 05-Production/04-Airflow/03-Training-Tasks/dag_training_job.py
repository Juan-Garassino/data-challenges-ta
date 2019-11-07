import datetime
from time import strftime

from airflow import DAG
from airflow.contrib.operators.mlengine_operator import MLEngineTrainingOperator
from airflow.operators.bash_operator import BashOperator

PROJECT_ID = "XXXXXX"
PACKAGE_NAME = "trainer"
BUCKET_NAME = "XXXXXX"
REGION = "europe-west1"
PYTHON_VERSION = "3.5"
RUNTIME_VERSION = "1.14"
FRAMEWORK = "scikit-learn"
MODEL_NAME = "taxi_fare_prediction_model"

PACKAGE_URI = "XXXXXX"


# ----------------------------------
# Sandbox Here
# ----------------------------------


# ----------------------------------
# DAG (Workflow) setup Here
# ----------------------------------

default_args = {'owner': 'airflow',
                'start_date': datetime.datetime.now() - datetime.timedelta(minutes=15),
                'concurrency': 1,
                'retries': 2}

dag = DAG('launch_training',
          default_args=default_args,
          schedule_interval='*/10 * * * *')

# ----------------------------------
# Tasks Definitions Here
# ----------------------------------

opr_hello = BashOperator(task_id='say_Hi',
                         bash_command='echo "Hi!!"',
                         dag=dag)

training_args = ["--scale-tier", "BASIC"]

launch_train = MLEngineTrainingOperator(
    task_id='ml_engine_training_op',
    project_id=PROJECT_ID,
    runtime_version=RUNTIME_VERSION,
    python_version=PYTHON_VERSION,
    package_uris=[PACKAGE_URI],
    job_id="taxi_fare_training_pipeline_{}".format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')),
    training_python_module='trainer.task',
    region=REGION,
    job_dir="gs://{}/trainings".format(BUCKET_NAME),
    training_args=training_args,
    dag=dag)

opr_hello >> launch_train
