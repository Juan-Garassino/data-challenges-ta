import unittest
import sqlite3

conn = sqlite3.connect('data/movies.sqlite') #??????
db = conn.cursor()

def artist_count(db): #to_refacto
  # TODO: use `db` to execute an SQL query against the database.

    request = '''SELECT COUNT(*) FROM artists'''
    results = db.execute(request)
    return results

def number_of_rows(db, table_name):
  # TODO: count number of rows in table table_name

    request = '''SELECT COUNT(*) FROM #{table_name}
    '''
    results = db.execute(request)
    return results

def sorted_artists(db):
  # TODO: return array of artists' names sorted alphabetically

    request = '''SELECT Name FROM artists ORDER BY Name
    '''
    results = db.execute(request)
    return results

def love_tracks(db):
  # TODO: return array of love songs' names

    request = '''SELECT Name FROM tracks WHERE Name LIKE '%love%' ORDER BY Name
    '''
    results = db.execute(request)
    return results

def long_tracks(db, min_length):
  # TODO: return an array of tracks' names verifying: duration > min_length (minutes) sorted by length (ascending)

    request = '''
    SELECT Name FROM tracks
    WHERE milliseconds > #{min_length} * 60000
    ORDER BY milliseconds ASC
    '''
    results = db.execute(request)
    return results
