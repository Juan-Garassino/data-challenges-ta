import unittest
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

def detailed_movies(db):
    # TODO: return the list of movie with their genre and director.

    request = '''
          SELECT movies.title, movies.genres, directors.name
          FROM movies
          INNER JOIN directors ON movies.director_id = directors.director_id
    '''
    results = db.execute(request)
    results = results.fetchall()
    return results

def stats_on(db, genre_name):
    # TODO: For the given genre of movie, return the number of movies and the average movie length in minutes (as a stats hash)

    request = '''SELECT movies.genres, COUNT(movies.title), ROUND(AVG(movies.minutes), 2)
    FROM movies
    WHERE movies.genres = "%s"
    ''' % genre_name
    stat = db.execute(request)
    stat = stat.fetchone()
    return {
      "genre": stat[0],
      "number_of_movies": stat[1],
      "avg_length": stat[2]
    } #?????

def top_five_artists(db, genre_name):
    # TODO: return list of top 5 directors with the most movies for a given genre.

    request = '''SELECT directors.name, COUNT(movies.title) AS movie_count
    FROM movies
    INNER JOIN directors ON movies.director_id = directors.director_id
    WHERE movies.genres = '%s'
    GROUP BY directors.name
    ORDER BY movie_count DESC
    LIMIT 5
    ''' % genre_name
    results = db.execute(request)
    results = results.fetchall()
    return results


# results = detailed_movies(db)
# print(len(results))
# print(results[0])
# results = stats_on(db, "Drama,Mystery")
results = top_five_artists(db, "Drama,Mystery")
print(results)
#for r in results:
#    print(r)
