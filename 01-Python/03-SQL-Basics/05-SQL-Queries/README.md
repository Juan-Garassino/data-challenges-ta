## Background & Objectives

Now it's time for something more complex. We'll be using `JOIN` queries to read data from multiple tables. To acquire instant Jedi skills in `JOIN` queries, [read this](http://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins) - the picture is really helpful.
## Specs

Complete the code in `sql_queries.rb`. Each method takes a `db` argument, which is an Cursor Object
on which you can call the `execute` method. Exactly like in the previous exercise.

### Detailed Tracks

- Implement `detailed_movies` to get all the movies title with the corresponding director name and genre name.
- Your output should be an array of arrays. **Hint:** you will have to use one `JOIN` sql statements.

This method should return an list of movies. Each element of this array would be an tuple: first element being the movies title, second element the movie director name, third element the movie's genre name.

### Statistics

For each genre of movie, find the stats, i.e. the number of movies and the average movie length (in minutes).

The method should return a Hash of statistics:

```python
results = stats_on(db, "Action,Adventure,Comedy")
print(results)
=> {
    'genre': 'Action,Adventure,Comedy',
    'number_of_movies': 153,
    'avg_length': 100.98
  }

```

### Top 5

Find the top 5 directos that made the most movies in a given genre. This method should return a listt of tuple with the director name and the number of movies of the given genre for each director.

```python
results = top_five_artists(db, "Action,Adventure,Comedy")
print(type(results[0]))
# => [('Robert Rodriguez', 5), ('Jonathan Frakes', 4), ('Anthony C. Ferrante', 3), ('Barry Sonnenfeld', 3), ('Jackie Chan', 3)]
```
