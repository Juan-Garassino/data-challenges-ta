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
    # query data from BQ and return data as dataframe
    pass
```
