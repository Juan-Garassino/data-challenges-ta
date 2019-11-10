## Delivery Time 

Estimated Time Arrival (ETA) is a key component of modern e-commerce services. It allows to manage customer expectations by displaying a predicted date for customer delivery. 

In this section, we will improve Olist ETA predictions and build a predictive model that will outperform the current version. 

Olist current model is shown in column `order_estimated_delivery_date` in the order dataset. 

Our variable to optimize is `wait_time`: the difference in days between the actual delivery date (`order_delivered_customer_date`) and the date of the order purchase (`order_purchase_timestamp`).

### Baseline

We first need to understand the baseline we want to optimize. 

- Plot `wait_time` and `expected_wait_time` distribution. What's the median difference ? 
- What's the `Mean Squared Error` for Olist's current ETA model? 

### First Model 

- Load `orders` training data and split it with a 30% test size in `X_train`, `X_test`, `y_train`, `y_test`. 

👉 Hint: make sure to drop variables `'order_id'` and variables `'wait_time', 'delay_vs_expected', 'expected_wait_time'` to avoid data leakage. 

👉 Hint: you can load existing order training set, with the command below: 

```python
from olist.order import Order 
orders = Order().get_training_data()
```

👉 Hint: you can also use the method `sklearn.model_selection.train_test_split` to easily split a dataset in training 

- Build a first prediction with the model of your choice. What's the best  `wait_time` you get? 

### More Features

We did a first pass at improving Olist ETA. Can we do better using additional features? 

- Create additional columns that correspond to the product category features at the order_id level. Does that increase the `mean_square_error` of your model? 

### Auto ML

Using the library [Tpot](http://epistasislab.github.io/tpot/), find the best model to optimize `wait_time`. What is the best `mean_square_error` you can achieve? 