## Background

In this challenge, we will learn the concepts of Mean, Mode, Median and Standard Deviation. To illustrate that, let us import a dataset to perform our statistics. We will be looking at the consumption of alcohol by country in 2010.

## The Mean and Variance
The sample **mean** (mu) is the average and is computed as the sum of all the observed outcomes  from the sample divided by the total number of events.
```python
n = len(samples)
mu = (1/n) * sum(samples)
```

The **standard deviation** (sigma) on the other hand is a statistical metric that describes the spread of the data, or how far the values are from the mean.
```python
n = len(samples)
sigma = ((1/(n - 1) * sum((samples - mu)**2))**0.5
```

Thanks to these definitions, implement the functions `mean(samples)` and `standard_deviation(samples)` in the file `basic_functions.py`. This functions take an array in arguments and return the mean and the standard deviation respectively.

## The Median
One problem when using the mean, is that it often does not depict the typical outcome. If one element from the sample is very far from the rest of the sample ("outlier"), then the mean will be affected because of this outlier. That's why, in some cases, we use **the Median**.

The median is the middle score :
- If we have an odd number of data, the median is the ..
- If we have an even number of data, the median is the ..

--> pour ce dataset tu devrais trouver : 6.40
##

TO DO:
- maximum
- minimum
-
