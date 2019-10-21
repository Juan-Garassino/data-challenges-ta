import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from google.cloud import storage

WORKFLOW_NAME = 'test'


# ----------------------------------
# Sandbox Here
# ----------------------------------
def test():
    BUCKET_NAME = "wagon-data"
    bucket = storage.Client().bucket(BUCKET_NAME)
    filename = "05_Production_TaxiFare_100000.csv"
    blob = bucket.blob(filename)
    blob.download_to_filename(filename)

    with open(filename, 'r') as train_data:
        df = pd.read_csv(train_data)
    print(df.shape)
    print('python function working')


# ----------------------------------
# DAG (Workflow) setup Here
# ----------------------------------
default_args = {'owner': 'airflow',
                'start_date': datetime.datetime.now() - datetime.timedelta(minutes=20),
                'concurrency': 1,
                'retries': 2}

dag = DAG('storage_download',
          default_args=default_args,
          schedule_interval='*/10 * * * *')

opr_hello = BashOperator(task_id='say_Hi',
                         bash_command='echo "Hi!!"',
                         dag=dag)
test_python = PythonOperator(task_id='test_python',
                                python_callable=test,
                                dag=dag)

opr_hello >> test_python
