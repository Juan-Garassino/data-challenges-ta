## Background & Objectives

Now we are going to dive into `JOIN` queries to read data from multiple tables. Again [this picture](http://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins) on `JOIN` queries is really helpful.

## Specs

Complete the code in `join_queries.py`. Each method takes a `db` argument, which is an Cursor Object on which you can call the `execute` method. Exactly like in the previous exercise.

There are three methods to implement:

### Detailed Orders
- Implement `detailed_orders` to get the shiper name and customer first name of all the orders made.

### Spent per Customer
- Implement `spent_per_customer` to get the total amount spent per customer - in ascending order.

### Who sell the most ?
- Implement `best_employee method` to determine who's the best employee! By "best employee", we mean the one who sell the most. 👑
