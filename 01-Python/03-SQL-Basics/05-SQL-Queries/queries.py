# pylint: disable=C0103, missing-docstring

def detailed_movies(db):
    # return the list of movies with their genres and director name
    query = """
        SELECT movies.title, movies.genres, directors.name
        FROM movies
        JOIN directors ON movies.director_id = directors.id
    """
    return db.execute(query).fetchall()

def top_five_youngest_newly_directors(db):
    # return the top 5 youngest directors when they direct their first movie
    query = """
        SELECT
            directors.name,
            movies.start_year - directors.birth_year age
        FROM directors
        JOIN movies ON directors.id = movies.director_id
        WHERE age IS NOT NULL
        ORDER BY age
        LIMIT 5
    """
    return db.execute(query).fetchall()

def late_released_movies(db):
    # return the list of all movies released after their director death
    query = """
        SELECT movies.title
        FROM directors
        JOIN movies ON directors.id = movies.director_id
        WHERE (movies.start_year - directors.death_year) > 0
        ORDER BY movies.title
    """
    results = db.execute(query).fetchall()
    return [movie[0] for movie in results]

def stats_on(db, genre_name):
    # return a dict of stats for a given genre
    query = """
        SELECT
            COUNT(*),
            AVG(minutes)
        FROM movies
        WHERE genres = ?
    """
    result = db.execute(query, (genre_name,)).fetchone()
    return {
        "genre": genre_name,
        "number_of_movies": result[0],
        "avg_length": round(result[1], 2)
    }


def top_five_directors_for(db, genre_name):
    # return the top 5 of the directors with the most movies for a given genre
    query = """
        SELECT
            directors.name,
            COUNT(*) movie_count
        FROM movies
        JOIN directors ON movies.director_id = directors.id
        WHERE genres = ?
        GROUP BY directors.name
        ORDER BY movie_count DESC, directors.name
        LIMIT 5
    """
    return db.execute(query, (genre_name,)).fetchall()

def movie_duration_buckets(db):
    # return the movie counts grouped by bucket of 30 min duration
    query = """
        SELECT
            (minutes / 30 + 1)*30 time_range,
            COUNT(*)
        FROM movies
        WHERE minutes IS NOT NULL
        GROUP BY time_range
    """
    return db.execute(query).fetchall()
