 Objective #1

Learn how to use BiGQuery

## Create a new dataset and import the data

- Data is available in an public table into Big Query `wagon-bootcamp-256316.taxifareEU.taxi_trips`
- Create a new dataset within your own BigQuery.
- Run your a SQL query that will create a table from the result of a query on `wagon-bootcamp-256316.taxifareEU.taxi_trips` into a table within your newly created dataset.
```sql
create table XXXXX 
select * from wagon-bootcamp-256316.taxifareEU.taxi_trips 
```
**NB**: If the table is not available anymore you can still create your table by uploading your training dataset from Storage 

## Query the data

- check the size of the data is correct:
```sql
select count(*) from your-projectid.dataset.tablename 
```
**NB** Note that the data is slightly different from kaggle data, a column `test` has been added in order to easily filter out data from traing or test set in the future

# Objective #2

Use python API to interact with **BigQuery**

## Install python package to query BigQuery

To load data from BiQuery you will need to use the python API.
For that, install `google-cloud-bigquery` with:

```bash
pip install --upgrade google-cloud-bigquery
pip show google-cloud-bigquery 
``` 
Inspect the version of google-cloud-bigquery, keep it in mind as you'll probably need to add it to a setup.py fil for the nest exercices ;) 
## Query Data programmatically

```python
from google.cloud import bigquery
client = bigquery.Client()
```
check [Big Query Documentation](https://googleapis.dev/python/bigquery/latest/index.html),
implement `get_data_from_bg()` function to query data from BQ from python:

```python
def get_data(N=100, test=False):
    # query data from BQ and return data as dataframe
    # param N, number of rows to query
    # param test, get test data if set to True
    # return, DataFrame
    pass
```
Now implement a function to insert data into BigQuery Table:
```python
def load_bq_table_from_df(df, dataset, table):
    # Load dataframe into Big Query Table, append to Table if already exists and Create Table it not
    # param df,
    # param dataset, dataset name
    # param table, table name
    # return
```
Test your 2 functions and verify the actually do what you implemnented them for
