## Create Environement

Create a Gloud Composer account on [GCP](https://console.cloud.google.com/composer), and create an environment named after you.  

Fill in following parameters:
- machine type : **n1-standard-1**  (check [Doc on machine Types](https://cloud.google.com/compute/docs/machine-types))
- disk size : **100 GB**
- image version : **composer-1.9.0-airflow-1.10.6**

Go to the Airflow Web Server interface and visualize your Airflow 

_NB : Airflow uses Compute Engine resources (3 by default), it is expensive if you let it run for a week, so don't forget to delete your Airflow session at the end of the day._

## Update your first workflow
Complete first_dag.py file:
- fill in `test()` function (try to implement at least a `print()` inside it)
- fill in the cron scheduler to launch dag every 2 minutes [help HERE](https://crontab.guru/)

## Upload DAG online
Inspect Makefile, fill correct environment variables and run:
```bash
make upload_dags
```
Here gcp took `first_dag.py` and placed it somewhere in a Bucket he created for you (you can check on you Storage, you'll see new buckets)
Airflow instance running via Composer refreshes every minute abd check for new dags inside that bucket  
If he finds one, He updates

You can check on Airflow web interface now

Check the dags details and try to visualize the output of `print()`
Go to your you environment on Google Cloud console, open Airflow webserver link and visualize your DAG, did it run properly ? 

## Good to know
**NB** you probably noticed you had a requirements.txt file and a  `make upload_python_libs`, don't run it for now but be aware that when you'll need to call external libraries inside you dag.py files, you will need to update your Airflow environement.
Meaning you will need to complete requirements.txt and run `make upload_python_libs`
Don't do it now as this action takes about 20 minutes tu update (you picked 1-cpu-3.5gram nodes)  

If you have troubles debugging your DAGS read this [mediump post](https://www.astronomer.io/blog/7-common-errors-to-check-when-debugging-airflow-dag/)
