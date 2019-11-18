## Product Categories with Logit

In this section we want to understand, using a logistic regression, which product categories tend to have higher 1 star reviews.

- Import the `order` training set with the following command: 

```python
from olist.order import Order 
Order().get_training_data()
``` 

- Run a logistic regression to predict `dim_is_one_star` on `product_category`. Which category have higher odds to get `one_star` reviews? 

