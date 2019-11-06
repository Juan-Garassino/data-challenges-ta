# Objective

Use python API to interact with **BigQuery**

## Install python package to query BigQuery

To load data from BiQuery you will need to use the python API.
For that, install `google-cloud-bigquery` with:

```bash
pip install --upgrade google-cloud-bigquery
``` 

## Query Data programmatically

```python
from google.cloud import bigquery
client = bigquery.Client()
```
check [Big Query Documentation](https://googleapis.dev/python/bigquery/latest/index.html),
implement get_data_from_bg function:

```python
def get_data(N=100, test=False):
    """
    query data from BQ and return data as dataframe
    :param N: number of rows to query
    :param test: get test data if set to True
    :return: DataFrame
    """
    pass
```

Now implement a function to insert data into BigQuery Table:

```python
def load_bq_table_from_df(df, dataset, table):
    """
    Load dataframe into Big Query Table, append to Table if already exists and Create Table it not
    :param df:
    :param dataset: dataset name
    :param table: table name
    :return:
    """
```
