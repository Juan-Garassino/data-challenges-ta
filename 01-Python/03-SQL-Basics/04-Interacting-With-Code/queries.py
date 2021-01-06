# pylint: disable=missing-docstring, C0103

def directors_count(db):
    # Return the number of directors contained in the database
    query = """
        SELECT COUNT(*)
        FROM directors
    """
    result = db.execute(query).fetchone()
    return result[0]


def directors_list(db):
    # Return the list of all the directors sorted in alphabetical order
    query = """
        SELECT name
        FROM directors
        ORDER BY name
    """
    results = db.execute(query).fetchall()
    return [element[0] for element in results]


def love_movies(db):
    # Return the list of all movies which contain the word "love" in their title, sorted in alphabetical order
    query = """
        SELECT title
        FROM movies
        WHERE title LIKE '%love%'
        ORDER BY title
    """
    results = db.execute(query).fetchall()
    return [element[0] for element in results]


def directors_named_like_count(db, name):
    # Return the number of directors which contain a given word in their name
    query = """
        SELECT COUNT(*)
        FROM directors
        WHERE name LIKE ?
    """
    result = db.execute(query, (f"%{name}%",)).fetchone()
    return result[0]


def movies_longer_than(db, min_length):
    # Return this list of all movies which are longer than a given duration, sorted in the alphabetical order
    query = """
        SELECT title
        FROM movies
        WHERE minutes > ?
        ORDER BY minutes
    """
    results = db.execute(query, (min_length,)).fetchall()
    return [element[0] for element in results]
