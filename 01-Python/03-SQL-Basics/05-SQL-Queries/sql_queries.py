# pylint: disable=c0103
def detailed_movies(db):
    # TODO: return the list of movies with their genre and director.
    request = '''
          YOUR SQL REQUEST HERE
    '''
    # execute your SQL request
    results = db.execute(request)

    # cursor.fetchall() fetches all the rows of a query result.
    # It returns all the rows as a list of tuples
    results = results.fetchall()
    return results

def stats_on(db, genre_name):
    # TODO: For the given genre of movie, return the number of movies and the average movie length in minutes (as a stats hash)
    # NOTE : It should return a dict : {"genre": stat[0],"number_of_movies": stat[1],"avg_length": stat[2]}

    pass

def top_five_artists(db, genre_name):
    # TODO: return list of top 5 directors with the most movies for a given genre.
    pass

