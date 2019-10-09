def directors_count(db):
    # TO-DO: use 'db' to execute an SQL query against the database.
    # Return directors count in database.

    request = 'SELECT COUNT(*) FROM directors;'
    results = db.execute(request)
    return results.fetchone()[0]

def number_of_rows(db, table_name):
    # TO-DO: count number of rows in table table_name

    request = f'SELECT COUNT(*) FROM {table_name}'
    results = db.execute(request)
    return results.fetchall()

def sorted_directors(db):
    # TO-DO: return a list of directors' names sorted alphabetically

    request = 'SELECT name FROM directors ORDER BY name'
    results = db.execute(request)
    return results

def love_movies(db):
    # TO-DO: return a list of love movies' names

    request = 'SELECT title FROM movies WHERE title LIKE "%love%" ORDER BY title'
    results = db.execute(request)
    return results

def long_movies(db, min_length):
    # TO-DO: return a list of movies' names
    # verifying: minutes > min_length, sorted by length (ascending)

    request = '\
      SELECT title FROM movies\
      WHERE minutes > {min_length}\
      ORDER BY minutes ASC\
    '
    results = db.execute(request)
    return results
