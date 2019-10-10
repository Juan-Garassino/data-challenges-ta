## Background & Objectives

Now we are going to dive into `JOIN` queries to read data from multiple tables. Again [this picture](http://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins) on `JOIN` queries is really helpful.

## Specs

👉 Complete the code in `join_queries.py`. Each method takes a `db` argument, which is a Cursor Object on which you can call the `execute` method. Exactly like in the previous exercise.

There are four methods to implement:

### Detailed Orders

👉 Implement `detailed_orders` to get the shipper name and the customer first name of all the orders made.

### Spent per Customer

👉 Implement `spent_per_customer` to get the total amount spent per customer - in ascending order. 👌

### Who sell the most ?

Implement `best_employee method` to determine who's the best employee! By "best employee", we mean the one who sell the most. 👑
We want the function to return a value like: `[('FirstName', 'LastName', sum_of_all_purchase (ex: 6000))]`

### Who doesn't buy anything?
Implement `orders_per_customer` to get the amount of Orders made by each Customer. As you can guess with the title, you should also display customer(s) with no order?

**Hint**: JOIN LEFT could be usefull. And in this case, the driving table is important...
