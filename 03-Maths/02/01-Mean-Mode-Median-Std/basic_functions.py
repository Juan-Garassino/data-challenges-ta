
def mean(samples):
    mu = 0
    for sample in samples:
        mu += sample
    return (mu/len(samples))

def standard_deviation(samples):
    squared_sum = 0
    mu = mean(samples)
    for sample in samples:
        squared_sum += (sample - mu)**2
    return ((1/(len(samples)-1)) * squared_sum)**0.5

import pandas as pd
data_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv')
alcohol_list = data_df["alcohol"].tolist()


print(mean(alcohol_list))

print(standard_deviation(alcohol_list))

import statistics
print("Standard Deviation of sample is % s "
                % (statistics.stdev(alcohol_list)))
