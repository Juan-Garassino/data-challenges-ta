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

who was the youngest director when directing his first movie?

SELECT
    directors.name,
    movies.start_year - directors.birth_year age
FROM directors
JOIN movies ON directors.id = movies.director_id
WHERE age IS NOT NULL
ORDER BY age
LIMIT 10

Adam Paloian    8
Alfonso Ribeiro 19
Kenn Navarro    20
Xavier Dolan    20
Albert Hughes   21
Xavier Dolan    21
Sam Raimi   22
John Singleton  23
Albert Hughes   23
Josef Fares 23

The first answers seem strange. Why?

which are the movies that were never watched by their director in a theatre?

SELECT
    movies.title
FROM directors
JOIN movies ON directors.id = movies.director_id
WHERE (movies.start_year - directors.death_year) > 0

Fantasia 2000
Game of Death
The Many Adventures of Winnie the Pooh
The Rescuers
Cars
Waitress

What are the 10 best movies of all time?

