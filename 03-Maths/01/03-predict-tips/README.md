‼️ Do not use numpy for this challenge

## Background
Well done, you have coded by yourself some of the tools we'll use very often during the next weeks.

As you will discover, Pandas helps you a lot with all this stuff and you will be able to transpose, multiple, invert,... a matrix in just one line of code.

But still, what you did is very useful to understand how it works, remember the formulas, and don't use them as a black box.

In this challenge, we try to give you a better intuition of how to use these tools through a "real" situation. The goal of this exercise is to make use of the functions we implemented in the previous sections and predict the tips waiters receive depending on different parameters.

## 1. Check the data
Before trying to create a model or start to solve any problem it's always a good idea to analyse the data (check the columns, the type of values, plot some beautiful graphs). Open jupyter notebook :

`jupyter notebook`

And go to the `predict-tips.ipynb` Notebook we prepared for you. You should see a first cell :

```
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")
tips.head()
```

Basically, we are loading the libraries and the dataset from Seaborn we'll use in this exercise. Our objective for this challenge is to predict the `tip` based on the `total_bill`.

Start by exploring and vizualizing the data :
- plot any graphs and retrieve any data from the dataset that could give you a better understanding of the dataset;
- plot the points with **total_bill on the X-Axis** and the corresponding **tip on the Y-Axis**;

## 2. Choose the best parameters

During the next weeks, we will learn different models (Linear Regression, KNN, Logistic Regression, Neural Networks,...). A important part of your job consists in choosing the right model and optimize the parameters to make the best predictions.

For your information, in this exercise we are using a Linear Regression model with one feature (total_bill). Basically, that means that we want to choose the best parameters (slope and intercept) to predict the tip the waiter will receive:

`tip = slope * total_bill + intercept`

- **In your Notebook**, implement the function `plot_line(slope, intercept, ax)` that plot a line with the `slope` and `intercept` arguments on the `ax` figure. We add the argument ax, so you can plot the line(s) on your scatterplot.

When you are done play with different value for `slope` and `intercept` in order to get a "good linear approximation" of the data. Can you find the best fit?

Not so easy (and not very "scientific"), right?

## 3. Compute the Mean Squared Error (MSE)
To answer this question, we will compute the Mean Squared Error. So, for each data in our dataset, we should evaluate the squared error:
`
predicted_tip = slope * total_bill + intercept
error = (predicted_tip - tip)**2
`
To answer this question, implement the functions in the `compute_error.py` file :
- `squared_errors(slope, intercept, total_bills, tips)` : return an array containing the squared errors between all predicted_tips and the actual_tips (from the dataset);
- `mean_squared_error(squared_errors)` : return the mean of the array contained in squared_errors.

When the `make` command passes the tests related to these 2 functions, go back to your Notebook. Now you can import these 2 functions and use them.

Again, play with different values for `slope` and `intercept` and try to get the best fit (in other words, try to find the slope and intercept that returns the smallest mean_error)

For your information, the best fit should return :
`mean_squared_error = 1.036`

Try to get close to this value.

## 4. Choose the best parameters
Ok, now we have a number (the Mean Squared Error) to quantify the precision of our model. But how can we get the **best parameters**? As you can guess, in the Data Scientist World, we need a better and faster way to get them.

During the next weeks, you will learn some algorithm to do that (Gradient Descent, Normal Equation,...). And you will discover the power of Scikit-learn that allows you to :
- Train a model with the data
- Make predictions based on this model


<details><summary markdown='span'>Discover Scikit-learn
</summary>
Insert these lines into your Notebook.

```python
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(tips[["total_bill"]], tips["tip"])
print(reg.coef_)
print(reg.intercept_)
```

`reg.coef_` is the slope of your model and `reg.intercept_` is the intercept. Try to insert these value in your `plot_line()`, `squared_errors()` and `mean_squared_error()` functions. What do you get?
</details>

