## Background & Objectives

In this section, we will cover the SQL `PARTITION BY` clause and the difference with `GROUP BY` in a `SELECT` statement. You will also explore several use cases of SQL `PARTITION BY`.

SQL `PARTITION BY` is used to divide the result set into partitions and perform computation on each subset of the partitioned data.

## Specs

### Group By Customers

SQL `GROUP BY` clause is used to group results by a specified column.

👉 Implement `group_by_customer()` to get the following values:
- Average order value per customer
- Minimum order value per customer
- Maximum order value per customer
- Sum of all orders per customer

### Partition By Customers

The SQL `PARTITION BY` clause can be used with the:
- OVER clause: to specify the column on which to perform aggregation
- RANK clause: to have the rank of each row.

In the previous example, we have used `GROUP BY` for the CustomerID column and calculated average, minimum, maximum values and total.

Let's switch to a similar scenario with the SQL `PARTITION BY` and `RANK` clauses to group results by customer.

👉 Implement the function `partition_by_customer()` to get the following values for each orderDetail:
- the CustomerID
- the Quantity
- the UnitPrice
- the TotalPrice (Quantity * UnitPrice)
- the Rank

Then **rank** the OrderDetails of each order by their total price (Quantity * UnitPrice) and return the products which rank is less than or equal to 2:


