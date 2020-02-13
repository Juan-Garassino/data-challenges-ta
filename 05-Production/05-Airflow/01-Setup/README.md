## Create Environement

Create a Gloud Composer account on [GCP](https://console.cloud.google.com/composer), and create an environment named after you.  

Go to the Airflow Web Server interface and visualize your Airflow 

_NB : Airflow uses Compute Engine resources (3 by default), it is expensive if you let it run for a week, so don't forget to delete your Airflow session at the end of the day._

## Update your first workflow
Complete first_dag.py file:
- fill in test() function
- fill in the cron scheduler to launch dag every 2 minutes [help HERE](https://crontab.guru/)

## Upload DAG online
Inspect Makefile, fill correct environment variables and run:
```bash
make upload_dags
```

Go to your you environment on Google Cloud console, open Airflow webserver link and visualize your DAG, did it run properly ? 

