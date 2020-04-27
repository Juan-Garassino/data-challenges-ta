import datetime

from airflow import DAG
from airflow.contrib.operators.mlengine_operator import MLEngineTrainingOperator
from airflow.operators.bash_operator import BashOperator

PROJECT_ID = "XXXX"
BUCKET_NAME = "XXXX"
REGION = "europe-west1"
PACKAGE_NAME = "TaxiFareModel"
FILENAME = "trainer"
PYTHON_VERSION = "3.7"
RUNTIME_VERSION = "1.15"
FRAMEWORK = "scikit-learn"

PACKAGE_URI = "gs://{}/trainings/code/airflow/{}-1.0.tar.gz".format(BUCKET_NAME, PACKAGE_NAME)

# ----------------------------------
# DAG (Workflow) setup Here
# ----------------------------------

default_args = {'owner': 'airflow',
                'start_date': datetime.datetime.now() - datetime.timedelta(minutes=20),
                'concurrency': 1,
                'retries': 2,
                'catchup': False}

dag = DAG('launch_training',
          default_args=default_args,
          schedule_interval='TODO')

# ----------------------------------
# Tasks Definitions Here
# ----------------------------------

opr_hello = BashOperator(task_id='say_Hi',
                         bash_command='echo "Hi!!"',
                         dag=dag)

training_args = ["--scale-tier", "BASIC"] # check doc https://cloud.google.com/ai-platform/training/docs/machine-types

launch_train = MLEngineTrainingOperator(
    task_id='ml_engine_training_op',
    project_id=PROJECT_ID,
    runtime_version=RUNTIME_VERSION,
    python_version=PYTHON_VERSION,
    package_uris=PACKAGE_URI,
    job_id="taxi_fare_training_pipeline_{}".format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')),
    training_python_module='{}.{}'.format(PACKAGE_NAME, FILENAME),
    region=REGION,
    job_dir="gs://{}/trainings".format(BUCKET_NAME),
    training_args=training_args,
    dag=dag)

opr_hello >> launch_train
