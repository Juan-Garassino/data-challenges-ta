## Background & Objectives
In this section, we cover the SQL PARTITION BY clause and, in particular, the difference with GROUP BY in a select statement. Through these exercises, you will also explore several use case of SQL PARTITION BY.

We use SQL PARTITION BY to divide the result set into partitions and perform computation on each subset of partitioned data.

## Specs
### Group By Customers
We use SQL GROUP BY clause to group results by specified column. For this exercise you have to implement the function group_by_customer() to get the following values:
- Average order value per customer
- Minimum order value per customer
- Maximum order value per customer
- Sum of all orders per customer

### Partition By Customers
We can use the SQL PARTITION BY clause with the:
- OVER clause: to specify the column on which we need to perform aggregation
- RANK clause: to have a row number of each row.

In the previous example, we used Group By with CustomerID column and calculated average, minimum, maximum values and total.

Let us rerun a similar scenario with the SQL PARTITION BY and RANK clauses to group results by customer. Implement the function partition_by_customer() to get the following values for each orderDetail:
- the CustomerID
- the Quantity
- the UnitPrice
- the TotalPrice (Quantity * UnitPrice)
- the Rank


### TO DO
- Rank the OrderDetails in each Order by their total price (Quantity * UnitPrice) and return products with rank less than or equal to 2:

SELECT * FROM (
 SELECT
 product_id,
 product_name,
 brand_id,
 list_price,
 RANK () OVER (
 PARTITION BY brand_id
 ORDER BY list_price DESC
 ) price_rank
 FROM
 production.products
) t
WHERE price_rank <= 3;
