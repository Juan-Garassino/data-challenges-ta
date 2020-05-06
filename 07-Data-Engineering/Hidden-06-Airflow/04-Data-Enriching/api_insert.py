import pandas as pd
import requests
from google.cloud import bigquery

ApiKey = "YOUR_KEY"


def json_format(j):
    fields_to_keep = ['date', 'maxtempF', 'mintempF', 'totalSnow_cm', ]
    j = {k: v for k, v in j.items() if k in fields_to_keep}
    return j


class weather_api(object):
    def __init__(self, api_key=ApiKey):
        self.url = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx'
        self.apikey = api_key

    def get_day_data(self):
        zones = self.url
        header = {"key": self.apikey,
                  "q": "New+York",
                  "date": 'XXXX',
                  "enddate": "XXX",
                  "format": "json"
                  }
        response = requests.get(zones, params=header).json()
        return response


def load_bq_table_from_df(df, dataset, table):
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset)
    table_ref = dataset_ref.table(table)
    r = client.load_table_from_dataframe(df, table_ref).result()
    return r

def load_rows_to_bq():
    client = bigquery.Client()
    table = client.get_table()  # Make an API request.
    rows_to_insert = [(u"Phred Phlyntstone", 32), (u"Wylma Phlyntstone", 29)]

    errors = client.insert_rows(table, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")

def enriching_datasets():
    DATASET = 'XXXX'
    TABLE = 'weather_crawling'
    api = weather_api()
    r = api.get_day_data()
    res = []
    for j in r['data']['weather']:
        res.append(json_format(j))
    df = pd.DataFrame(res)
    df = df.rename(columns={'date': 'DATE', 'maxtempF': 'TMAX', 'mintempF': 'TMIN', 'totalSnow_cm': 'SNWD'})
    load_bq_table_from_df(df, DATASET, TABLE)
    print("inserted data into table")


if __name__ == '__main__':
    enriching_datasets()
