import unittest
import sqlite3

conn = sqlite3.connect('data/ecommerce.db') #??????
db = conn.cursor()

def detailed_tracks(db):
  # TODO: return the list of tracks with their album and artist.

  request = '''SELECT tracks.name, albums.title, artists.name
    FROM tracks
    INNER JOIN albums ON tracks.album_id = albums.id
    INNER JOIN artists ON albums.artist_id = artists.id
    '''
    results = db.execute(request)
    return results

def stats_on(db, genre_name):
  # TODO: For the given category of music, return the number of tracks and the average song length (as a stats hash)

  request = '''SELECT genres.name, COUNT(tracks.name), ROUND(AVG(milliseconds) / 60000, 2)
    FROM tracks
    INNER JOIN genres ON genres.id = tracks.genre_id
    WHERE genres.name = '#{genre_name}'
    '''
    results = db.execute(request)
    return results
    return {
      category: stat[0],
      number_of_songs: stat[1],
      avg_length: stat[2]
    } #?????

def top_five_artists(db, genre_name):
  # TODO: return list of top 5 artists with the most songs for a given genre.

  request = '''SELECT artists.name, COUNT(tracks.name) AS track_count
    FROM tracks
    INNER JOIN albums ON tracks.album_id = albums.id
    INNER JOIN artists ON albums.artist_id = artists.id
    INNER JOIN genres ON tracks.genre_id = genres.id
    WHERE genres.name = '#{genre_name}'
    GROUP BY artists.name
    ORDER BY track_count DESC
    LIMIT 5
    '''
    results = db.execute(request)
    return results
