## Background & Objectives

## Specs
### Average per Customer
We will start by calculating the average amount spent per customer.
- implement the `get_average_purchase(db)` to get ...
Hint : GROUP BY, AVG

### General Average
Now, we would like to calculate the general average for the OrderDetail.
- implement the `get_general_avg_order(db)` to get ...

### Who are the best buyer?
Now we would like to know who are the customers who buy more than the general average. That means the customer with average_amount_spent_per_customer > general_average.

Can you see that the main part has already been done in the 2 previous questions? We could (and should) reuse our previous code (copy/paste) and insert it into the WITH clause.

- Using the WITH clause, can you implement the function display_new_columns(db) and return a list containing all the ID's and the average amount spent per customer?
`
display_best_buyers(db)
=> [(572.91, 2), (870.01, 4), (548.15, 5)]
`

Meaning that the customer 2 spent on average 572,91eur per Order
### TO DO
