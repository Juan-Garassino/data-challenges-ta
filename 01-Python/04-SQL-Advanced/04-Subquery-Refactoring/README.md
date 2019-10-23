## Background & Objectives

In the section we will discover subquery-refactoring! Indeed we may need to nest previous SQL queries coded into a new one to reduce repetition and simplify complex SQL statements. This is performed by the `WITH`. 👌

## Specs

### Average per Customer

👉 Implement `get_average_purchase` to get the average amount spent per customer (by ascending CustomerID).

### General Average

👉  Implement`get_general_avg_order` to get the average order in terms of price.

### Who are the best buyers?

Now let's find the customers who have made bigger order than the average (average_purchase_per_customer > general_average_purchase).

Can you see that the main part has already been done in the 2 previous questions? Let's use our previous queries thanks to the `WITH` clause.

👉 Implement the function `display_best_buyers` to get all the ID's and the average amount of these best buyers!

You should get this:

```python
display_best_buyers(db)
=> [(572.91, 2), [...], (548.15, 5)]
```

Meaning that the customer with ID 2 spent on average €572,91 per Order
