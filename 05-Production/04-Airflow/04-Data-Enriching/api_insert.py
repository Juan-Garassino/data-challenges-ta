import requests
import pandas as pd
from google.cloud import bigquery
from datetime import date

ApiKey = "a128fc3fde7e4981b7e181259190411"


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
                  # Fill Here missing fields
                  "format": "json"
                  }
        response = requests.get(zones, params=header).json()
        return response


def load_bq_table_from_df(df, dataset, table):
    """
    Fill in Here
    :param df:
    :param dataset:
    :param table:
    :return:
    """
    pass


if __name__ == '__main__':
    DATASET = 'GMBInput'
    TABLE = 'NY_weather_forecast'
    api = weather_api()
    r = api.get_day_data()
    res = []
    for j in r['data']['weather']:
        res.append(json_format(j))
    df = pd.DataFrame(res)
    df = df.rename(columns={'date': 'DATE', 'maxtempF': 'TMAX', 'mintempF': 'TMIN', 'totalSnow_cm': 'SNWD'})
    load_bq_table_from_df(df, DATASET, TABLE)
