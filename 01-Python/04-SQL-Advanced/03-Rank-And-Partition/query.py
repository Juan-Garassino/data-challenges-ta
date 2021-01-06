# pylint:disable=C0111,C0103

def movie_duration_buckets(db):
    query = """
        SELECT
            (minutes / 30 + 1)*30 time_range,
            COUNT(*)
        FROM movies
        WHERE minutes IS NOT NULL
        GROUP BY time_range
    """
    return db.execute(query).fetchall()


def longest_movies_by_director(db, first_letter):
    query = """
        SELECT
            movies.title,
            directors.name,
            movies.minutes,
            RANK() OVER (PARTITION BY directors.name ORDER BY movies.minutes DESC) director_length_rank
        FROM movies
        JOIN directors ON movies.director_id = directors.id
        WHERE directors.name LIKE ?
    """
    return db.execute(query, (f"{first_letter}%",)).fetchall()


def top_3_longest(db, first_letter):
    query = """
        SELECT
            movies.title,
            directors.name,
            movies.minutes,
            RANK() OVER (PARTITION BY directors.name ORDER BY movies.minutes DESC) director_length_rank
        FROM movies
        JOIN directors ON movies.director_id = directors.id
        WHERE directors.name LIKE ?
    """
    return db.execute(query, (f"{first_letter}%",)).fetchall()

