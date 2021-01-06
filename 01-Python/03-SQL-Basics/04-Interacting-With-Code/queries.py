# pylint: disable=missing-docstring, C0103


def directors_count(db):
    # TO-DO: use 'db' to execute an SQL query against the database.
    # Return directors count in database.
    query = """
        SELECT COUNT(*)
        FROM directors
    """
    result = db.execute(query).fetchone()
    return result[0]


def sorted_directors(db):
    # TO-DO: return a list of directors' names sorted alphabetically
    query = """
        SELECT name
        FROM directors
        ORDER BY name
    """
    results = db.execute(query).fetchall()
    return [element[0] for element in results]


def love_movies(db):
    """TO-DO: return a list of movies with 'love' in the name, sorted
    alphabetically"""
    query = """
        SELECT title
        FROM movies
        WHERE title LIKE '%love%'
        ORDER BY title
    """
    results = db.execute(query).fetchall()
    return [element[0] for element in results]


def directors_with_name(db, name):
    # TO-DO: count the number of directors with a name like `name`
    query = """
        SELECT COUNT(*)
        FROM directors
        WHERE name LIKE ?
    """
    result = db.execute(query, (f"%{name}%",)).fetchone()
    return result[0]


def long_movies(db, min_length):
    """TO-DO: return a list of movie names
    verifying: minutes > min_length, sorted by length (ascending)"""
    query = """
        SELECT title
        FROM movies
        WHERE minutes > ?
        ORDER BY minutes
    """
    results = db.execute(query, (min_length,)).fetchall()
    return [element[0] for element in results]
