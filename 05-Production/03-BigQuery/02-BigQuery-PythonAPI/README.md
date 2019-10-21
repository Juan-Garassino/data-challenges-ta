## Install python package to query BigQuery

```bash
pip install --upgrade google-cloud-bigquery
```  

Then set up authentification

Then in any python file or notebook::

    from google.cloud import bigquery
    
    client = bigquery.Client()
    
    # Perform a query.
    QUERY = (
        'SELECT pickup_datetime FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    
    for row in rows:
        print(row.name)

