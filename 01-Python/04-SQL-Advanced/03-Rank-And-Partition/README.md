## Background & Objectives

In this section, we will cover the SQL `PARTITION BY` clause and the difference with `GROUP BY`in a `SELECT` statement. You will also explore several use cases of SQL `PARTITION BY`.

## Specs

### Bucketing The Movies Durations

First. What is a bucket?

"To 'bin' (or 'bucket') the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent, and are often (but not required to be) of equal size" - https://en.wikipedia.org/wiki/Histogram

👉 Implement `movie_duration_buckets()` to get the bucket of the movie duration of our database.


Hint 💡 :
`
movie_duration_buckets(db)
=> [(30, 292), (60, 764), (90, 1362), [...],(690, 2), (900, 1), (1020, 1)]
`


### Partition By Directors

The SQL `PARTITION BY` clause can be used with the:
- OVER clause: to specify the column on which we need to perform aggregation
- RANK clause: to have a row number of each row.

In the previous example, we used Group By with the Minutes column to bucket our data. Let's switch to a similar scenario with the SQL `PARTITION BY` and `RANK` clauses to group results by customer.

👉 Implement the function `longuest_movies_by_director()` to get the following values for each orderDetail:
- the CustomerID  - the CustomerID
- the Quantity  - the Quantity
- the UnitPrice - the UnitPrice
- the TotalPrice (Quantity * UnitPrice) - the TotalPrice (Quantity * UnitPrice)
- the Rank  - the Rank


Then **rank** the OrderDetails of each order by their total price (Quantity * UnitPrice) and return the products which rank is less than or equal to 2:
