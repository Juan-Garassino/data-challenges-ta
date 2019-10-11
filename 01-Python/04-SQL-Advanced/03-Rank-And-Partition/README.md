## Background & Objectives

In this section, we will cover the SQL `PARTITION BY` clause and its difference with `GROUP BY` in a `SELECT` statement. You will also explore the usecase of  the SQL `PARTITION BY` clause.

## Specs

### Bucketing The Movie Duration

First. What is a bucket?
To **'bin'** (or **'bucket'**) the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent, and are often (but not required to be) of equal size" - https://en.wikipedia.org/wiki/Histogram

👉 Implement `movie_duration_buckets()` to get the buckets of the movie duration of our database!<br>
A bucket contain a **count** of all the movies with a duration in the **range** of the bucket.<br>
For example, the bucket **30** will contain the count of all the movies with a duration between **0 min** and **30 min**.<br>
Or an other way to see it is:
- The value for bucket **30** should be equal to `SELECT COUNT(*) FROM movies WHERE minutes < 30;`

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

👉 Implement the function `longest_movies_by_director()` to find the longest movie of each director.<br>
Each rows returned by the query should look like:<br>
`('Movie Title', 'Director Name', movie_duration (ex: 120), rank (ex:2))`<br>
The **longuest movie** by a director should have the **rank 1** and the **shortest** should have the **last rank**.<br>

We expect a result like:

```python
longest_movies_by_director(db, "X")
=> [
      ('Laurence Anyways', 'Xavier Dolan', 168, 1),
      ('Mommy', 'Xavier Dolan', 139, 2),
      ('Tom at the Farm', 'Xavier Dolan', 102, 3),
      ('Heartbeats', 'Xavier Dolan', 101, 4),
        [...]
      ( 'Hitman', 'Xavier Gens', 100, 3)
    ]
```

### Top-3 longest movies

👉 Implement the function `top_3_longest()` to find the top-3 of longest movies. 👌 Let's **rank** them!
