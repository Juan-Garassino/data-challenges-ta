# pylint:disable=C0111,C0103

def movie_duration_buckets(db):
    request = """
        SELECT (minutes/30)*30+30 AS minute, count(id) FROM movies WHERE minutes IS NOT NULL GROUP BY minute ORDER BY minutes ASC
    """
    result = db.execute(request)
    return result.fetchall()

def longuest_movies_by_director(db, first_letter):
    request = """
        SELECT title, d.name, minutes, ROW_NUMBER() OVER (PARTITION BY d.id ORDER BY minutes DESC) AS rank
        FROM directors d JOIN movies m ON m.director_id = d.id WHERE d.name LIKE ? ORDER BY d.name, rank ASC
    """
    result = db.execute(request, (f"{first_letter}%",))
    return result.fetchall()


def top_3_longuest(db, first_letter):
    request = """
        SELECT * FROM (
        SELECT title, d.name, minutes, ROW_NUMBER() OVER (PARTITION BY d.id ORDER BY minutes DESC) AS rank
        FROM directors d JOIN movies m ON m.director_id = d.id WHERE d.name LIKE ? ORDER BY d.name, rank ASC
        )
        WHERE rank <= 3
    """
    result = db.execute(request, (f"{first_letter}%",))
    return result.fetchall()
