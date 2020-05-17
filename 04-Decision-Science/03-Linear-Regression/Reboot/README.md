## Reboot: Improving Estimated Delivery Time?

Estimated Time Arrival (ETA) is a key component of modern e-commerce services. It allows to manage customer expectations by displaying a predicted date for customer delivery.

In this section, we will improve Olist ETA predictions and build a predictive model that will outperform the current version.

Olist current model is shown in column `order_estimated_delivery_date` in the order dataset.

Our variable to optimize is `wait_time`: the difference in days between the actual delivery date (`order_delivered_customer_date`) and the date of the order purchase (`order_purchase_timestamp`).

### Baseline

We first need to understand the baseline we want to optimize.

- Plot `wait_time` and `expected_wait_time` distribution. What's the median difference ?
- What's the `RMSE` for Olist's current ETA model?

### First OLS model

Build a first prediction with the model of your choice. What’s the best wait_time you get?

### More Features

We did a first pass at improving Olist ETA. Can we do better using additional features?

- Create additional columns that correspond to the product category features at the order_id level. Does that increase the `RMSE` of your model?
