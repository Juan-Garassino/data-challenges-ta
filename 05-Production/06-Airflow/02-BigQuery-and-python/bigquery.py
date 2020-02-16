import googleapiclient
import pandas as pd
from google.cloud import bigquery, storage
from sklearn.externals import joblib

BUCKET_NAME = "wagon-data"

TABLE = "evaluation"
DATASET = "taxiFare"
BUCKET_NAME = "wagon-data"

model_folder = "pipeline_v3_bq"


def get_data_from_bq(N=10000, test=False, all=True):
    """
    qeury data from BQ and return data as dataframe
    :param N: number of rows to query
    :param test: get test data if set to True
    :return: DataFrame
    """
    pass

def load_bq_table_from_df(df, dataset, table):
    """
    Load dataframe into Big Query Table, append to Table if already exists and Create Table it not
    :param df:
    :param dataset: dataset name
    :param table: table name
    :return:
    """
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset)
    table_ref = dataset_ref.table(table)
    r = client.load_table_from_dataframe(df, table_ref).result()
    return r

