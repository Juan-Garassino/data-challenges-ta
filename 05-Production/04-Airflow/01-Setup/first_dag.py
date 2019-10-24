import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

WORKFLOW_NAME = 'test'


# ----------------------------------
# Sandbox Here
# ----------------------------------
def test():
    """
    Write our code Here
    :return:
    """
    print('python function working')


# ----------------------------------
# DAG (Workflow) setup Here
# ----------------------------------
default_args = {'owner': 'airflow',
                'start_date': datetime.datetime.now() - datetime.timedelta(minutes=20),
                'concurrency': 1,
                'retries': 2}

dag = DAG('test',
          default_args=default_args,
          schedule_interval='*/10 * * * *')

opr_hello = BashOperator(task_id='say_Hi',
                         bash_command='echo "Hi!!"',
                         dag=dag)
test_insertion = PythonOperator(task_id='test_python',
                                python_callable=test,
                                dag=dag)

opr_hello >> test_insertion
