## Multivariate Regression 🌞

In this section we will use a fixed effect logistic regression in order to measure which areas could yield the highest return to either maximize the share of 5 stars or minimize the share of 1 stars. 

We will use our training data, available after running: 

```python 
from olist.order import Order
data = Order().get_training_data()
```

### Exercices

- Center to the mean the following variables: 
  
  - `distance_seller_customer` 
  - `delay_vs_expected`
  - `wait_time`
  
- Create a training_set `x` that will contain the dependent variables and an additional column `intercept`. Create two Series `Y_five_star` and `Y_one_star` that contain target variables.
  
- Compute the correlation matrix for all features in `Order().get_training_data()`. Which features are highly correlated? 

**Predict five star**

- Plot side by side distribution plots for each variables, split by `dim_is_five_star`. Which features seem differentiating orders with or without five star? 

- Run a Logistic regression with target `dim_is_five_star`. Output the confusion matrix. How do you interpret the results of the logistic regression? 

**Predict one star**

- Plot side by side distribution plots for each variables, split by `dim_is_one_star`. Which features seem differentiating orders with or without five star? 

- Run a Logistic regression with target `dim_is_one_star`. Output the confusion matrix. How do you interpret the results of the logistic regression? 