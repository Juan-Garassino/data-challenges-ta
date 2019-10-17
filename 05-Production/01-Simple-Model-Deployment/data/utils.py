import json

import pandas as pd

NAME_JSON = 'test.json'
test = pd.read_csv('05_Production_TaxiFare_TEST_1000_with_answers.csv')

test = test.drop(['pickup_datetime', 'key', 'fare_amount'], axis=1)


def to_txt(test):
    test.to_csv('test.txt', header=None, index=None, sep=',', mode='a')


def to_list(test):
    test_lists = test.values.tolist()

    with open(NAME_JSON, 'w') as outfile:
        json.dump(test_lists, outfile)

to_txt(test)
