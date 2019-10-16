# Background
Well done, you have coded by yourself some of the tools we'll use very often during the next weeks.

As you will discover, Pandas helps you a lot with all this stuff and you will be able to transpose, multiple, invert,... a matrix in just one line of code.

But still, what you did is very useful to understand how it works, remember the formulas, and don't use them as a black box.

In this challenge, we try to give you a better intuition of how to use these tools through a "real" situation. The goal of this exercise is to use the functions we implemented in the previous sections and predict the tips waiters receive depending on different parameters.

## 1. Check the data
Before trying to create a model or start to solve any problem it's always a good idea to analyse the data (check the columns, the type of values, plot some beautiful graphs).

`jupyter notebook`

To simplify the problem, we will predict the tips based on the total_bill. Go into the `predict-tips.ipynd` we pre-filled for you and answer the following questions :
- plot the points with total_bill on the X-Axis and the corresponding tip on the Y-Axis?
- implement the function `plot_line(slope, intercept)` that plot a line with the slope and intercept arguments(on the same figure as the previous one).

## 2. Choose the best parameters

During the next weeks, we will learn different models (Linear Regression, KNN, Logistic Regression, Neural Networks,...). A important part of your job consists in choosing the right model and optimize the parameters to make the best predictions.

For your information, in this exercise we are using a Linear Regression model with one feature (total_bill). Basically, that means that we want to choose the best parameters (slope and intercept) to predict the tip the waiter will receive:

`tip = slope * total_bill + intercept`

- **In your Notebook**, implement the function `plot_line(slope, intercept)` that plot a line with the slope and intercept arguments(on the same figure as the previous one).

When you are done play with different value for `slope` and `intercept` in order to get a "good approximation". Can you find the best fit?

Not so easy (and not very "scientific"), right?

## 2. Compute the Mean Squared Error (MSE)
To answer this question, we will compute the Mean Error. So, for each data in our dataset, we should evaluate the squared error:
`
predicted_tips = slope * total_bills + intercept
errors = (predicted_tips - tips)**2
`
To answer this question, implement the functions in the `compute_error.py` file :
- `get_errors(slope, intercept, total_bills, tips)` :
- `mean_squared_error(errors)` :

When the `make` command passes the tests related to these 2 functions, go back to your Notebook. Now you can import these 2 functions and use them.

Again, play with different values for `slope` and `intercept` and try to get the best fit (in other words, try to find the slope and intercept that returns the smallest mean_error)

For your information, the best fit should return :
mean_squared_error = 1.036

## 3.

