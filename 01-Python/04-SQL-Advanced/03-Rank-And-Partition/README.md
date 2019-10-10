## Background & Objectives

In this section, we will cover the SQL `PARTITION BY` clause and its difference with `GROUP BY`in a `SELECT` statement. You will also explore the usecase of  the SQL `PARTITION BY` clause.

## Specs

### Bucketing The Movie Duration

First. What is a bucket?
To **'bin'** (or **'bucket'**) the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent, and are often (but not required to be) of equal size" - https://en.wikipedia.org/wiki/Histogram

👉 Implement `movie_duration_buckets()` to get the bucket of the movie duration of our database!


Hint 💡 :
```python
movie_duration_buckets(db)
=> [(30, 292), (60, 764), (90, 1362), [...],(690, 2), (900, 1), (1020, 1)]
```

### Partition By Directors

The SQL `PARTITION BY` clause can be used with the:
- OVER clause: to specify the column on which we need to perform aggregation
- RANK clause: to have a row number of each row.

In the previous example, we used `GROUP BY` with the Minutes column to bucket our data. Let's switch to a similar scenario with the SQL `PARTITION BY`.

👉 Implement the function `longest_movies_by_director()` to find the longest movie of each director.

Hint 💡 :
```python
longest_movies_by_director(db)
=> [[('Of Gods and Men', 'Xavier Beauvois', 122, 1), ('Laurence Anyways', 'Xavier Dolan', 168, 1), [...], ('Hitman', 'Xavier Gens', 100, 3)]
```

### Top-3 longest movies

👉 Implement the function `top_3_longest()` to find the top-3 of longest movies. 👌 Let's **rank** them!
