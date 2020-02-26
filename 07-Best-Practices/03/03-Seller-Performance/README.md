## 3. Sellers

In this section we look at seller performance on customer satisfaction.

### 3.1 Data preparation

- Create the method `get_training_data` in `olist/seller.py` that will return the following DataFrame:

  - `seller_id` (_str_) _the id of the product_
  - `seller_state` (_str_) _the state where seller is located_
  - `seller_city` (_str_) _the city where seller is located_
  - `delay_to_carrier` (_float_) _if the order is delivered after the shipping limit date, return the number of days between two dates, otherwise 0_
  - `seller_wait_time` (_float_) _Average number of days customers waited_
  - `share_of_five_stars` (_float_) _The share of five stars orders for orders in which the seller was involved_
  - `share_of_one_stars` (_float_) _The share of one stars orders for orders in which the seller was involved_
  - `seller_review_score` (_float_) _The average review score for orders in which the seller was involved_
  - `n_orders` (_int_) _The number of orders the seller was involved with._

### 3.2 Analysis

Open `notebooks/03_03_seller_performance.ipynb`and follows instructions (copied below)

Let's start by some initial exploratory analysis on sellers distribution:

- What's the median number of orders per seller? How is the distribution on that variable looking?
- What's the share of orders per seller state? Is it concentrated or distributed across Brazil?
- Run a correlation between variables, which insights do you draw from it?

**Delay to Carrier**

The variable `delay_to_carrier` measures the number of days between the shipping date limit imposed by Olist and the actual delivery date to the customer.

- What's the share of sellers that have an average `delay_to_carrier` above 0?
- Model out the impact of variable `delay_to_carrier` to `average_review_score`. What do you conclude?

**Seller location**

We now want to explore the impact of `seller_state` to `wait_time` and other variables:

- Plot a text_scatterplot for states that had more than 100 orders, with `n_orders` on the x axis and `wait_time` on the y axis.
- Model out the impact of each `seller_state` to variable `wait_time`. Which locations impact more `wait_time`?

**Review score**

All together now! Let's model out the impact of each variable to our target variable `avg_review_score`:

- Run an OLS model with `n_orders`, `seller_state` and `delay_to_carrier` as dependent variable and `avg_review_score` as the target variable
