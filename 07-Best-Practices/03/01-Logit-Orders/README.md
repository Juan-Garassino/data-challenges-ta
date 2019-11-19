## Orders with Logit

In this section we want to understand, using a logistic regression, which variables correlate to either 1 star reviews or 5 stars reviews. 

- Import the `order` training set with the following command: 

```python
from olist.order import Order 
Order().get_training_data()
``` 

### One Star

- Run a logistic regression to predict `dim_is_one_star` on variables `wait_time`, `expected_wait_time`, `number_of_products`, `number_of_sellers`, `price` and `distance_seller_customer`. 
- How do you interpret results? Which variables have higher impact on `dim_is_one_star` reviews? 

### Five Star

- Run a logistic regression to predict `dim_is_five_star` on variables `wait_time`, `expected_wait_time`, `number_of_products`, `number_of_sellers`, `price` and `distance_seller_customer`. 
- How do you interpret results? Which variables have higher impact on `dim_is_five_star` reviews? 