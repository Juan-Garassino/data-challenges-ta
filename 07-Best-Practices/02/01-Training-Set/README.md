### Training Set 🏋️‍

In this challenge, we will implement a method to return a training set at the order level. We will implement this training set in the `olist/order.py` file. This will come handy for our next modeling phase. 

#### Introduction 

Our goal is to create the following DataFrame: 

  - `order_id` (_str_) _the id of the order_
  - `wait_time` (_float_) _the number of days between order_date and delivered_date_
  - `wait_vs_expected` (_float_) _if the actual delivery date is later than the estimated delivery date, returns the absolute number of days between the two dates, otherwise return 0_
  - `dim_is_five_star` (_int_) _1 if the order received a five_star, 0 otherwise_
  - `dim_is_one_star` (_int_) _1 if the order received a one_star, 0 otherwise_
  - `number_of_product` (_int_) _number of products that the order contains_
  - `number_of_sellers` (_int_) _number of sellers involved in the order_
  - `freight_value` (_float_) _value of the freight paid by customer_
  - (Optional) `distance_customer_seller` (_float_) _the distance in km between customer and seller_

#### Exercices

- Implement each feature as a separate method within the `Order` class available at `olist/order.py` 

- Create a method `get_training_data()` that returns the complete DataFrame.