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

The median is the value separating the higher half from the lower half of a data sample (a population or a probability distribution). For a data set, it may be thought of as the **"middle" value**. For example, in the data set {1, 3, 3, 6, 7, 8, 9}, the median is 6, the fourth largest, and also the fourth smallest, number in the sample.

One problem when using the mean, is that it often does not depict the typical outcome. If one element from the sample is very far from the rest of the sample ("outlier"), then the mean will be affected because of this outlier. That's why, in some cases, we use **the Median**.

Read this [wikipedia article](https://en.wikipedia.org/wiki/Median) to see how the **median** is computed.

## The Quartiles

The **first quartile (Q1)** is defined as the middle number between the smallest number and the median of the data set. The **second quartile (Q2)** is the median of the data. The **third quartile (Q3)** is the middle value between the median and the highest value of the data set.

Read this [wikipedia article](https://en.wikipedia.org/wiki/Quartile) to see how the **quartiles** are computed.

## The Mode

The mode of a set of data values is the value that appears most often. In other words, it is the value that is most likely to be sampled.

Read this [wikipedia article](https://en.wikipedia.org/wiki/Mode_(statistics)) to see how the **mode** is computed.
