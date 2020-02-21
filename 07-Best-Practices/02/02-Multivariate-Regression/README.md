## Multivariate Regression 🌞

We are finally ready to start investigating explaining factors for customer satisfaction using our newly coded training data!

```python
from olist.order import Order
data = Order().get_training_data()
```

We will use a multivariate linear regression with [statsmodels](statsmodels.org) to measure order features importance on customer satisfaction.

Open `notebooks/02_02_mutivariate_regression.ipynb` and follows instructions (copied below)

### Prepare dataset

- Plot distribution plots for variable available in order training_set. What do you notice for variables `distance_seller_customer`, `price` and `freight_value` ?

- Scale the variables `distance_seller_customer`, `price` and `freight_value`

- Compute the correlation matrix for all features in `Order().get_training_data()`. Which features are correlated?

### Run univariate regression

- Run an OLS model `model1` where `review_score` is the target variable and `wait_time` is the dependent variable. Print the `summary` table: how do you interpret those results?

### Run multivariate regression

- Run an OLS model `model2` where `review_score` is the target variable and `wait_time`, `distance_seller_customer` and `price` are the dependent variables. Print the `summary` table: how do you interpret those results?

### Check model robustness

- For model1 and model2, plot residuals graphs and QQplot.
