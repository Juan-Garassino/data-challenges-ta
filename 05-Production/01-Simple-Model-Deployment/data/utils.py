import json

import pandas as pd
NAME_JSON = 'test.json'
test = pd.read_csv('05_Production_TaxiFare_TEST_1000_with_answers.csv')

test = test.drop(['pickup_datetime', 'key', 'fare_amount'], axis=1)
test_lists = test.values.tolist()

with open(NAME_JSON, 'w') as outfile:
    json.dump(test_lists, outfile)
