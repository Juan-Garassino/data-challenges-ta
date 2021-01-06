# pylint: disable=C0103, missing-docstring

def detailed_movies(db):
    """return the list of movies with their genre and director."""
    query = """
        SELECT movies.title, movies.genres, directors.name
        FROM movies
        JOIN directors ON movies.director_id = directors.id
    """
    return db.execute(query).fetchall()


def stats_on(db, genre_name):
    """For the given genre of movie, return the number of movies and the average
     movie length in minutes (as a stats hash)."""
    # NOTE : It should return a dict :
    #     {
    #         "genre": stat[0],
    #         "number_of_movies": stat[1],
    #         "avg_length": stat[2]
    #     }"""
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


def top_five_artists(db, genre_name):
    """return list of top 5 directors with the most movies for a given genre."""
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
