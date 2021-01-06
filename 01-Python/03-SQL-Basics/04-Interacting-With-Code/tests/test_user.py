# pylint: disable-all

import unittest
import sqlite3
from yaml import load, FullLoader
from os import path
from queries import directors_count, directors_list, love_movies,\
    directors_named_like_count, movies_longer_than

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
with open(path.join(path.dirname(__file__), 'results.yml'), encoding='utf-8') as f:
    results = load(f, Loader=FullLoader)

class QueriesMethods(unittest.TestCase):
    def test_directors_count(self):
        count = directors_count(db)
        self.assertIs(type(count), int)
        self.assertEqual(count, 4092)

    def test_directors_list(self):
        directors = results['directors']
        response = directors_list(db)
        self.assertIs(type(response), list)
        self.assertEqual(response, directors)

    def test_love_movies(self):
        love_movies_list = results['love_movies']
        response = love_movies(db)
        self.assertIs(type(response), list)
        self.assertEqual(response, love_movies_list)

    def test_directors_named_like_count(self):
        directors_count = directors_named_like_count(db, "kubric")
        self.assertIs(type(directors_count), int)
        self.assertEqual(directors_count, 1)
        directors_count = directors_named_like_count(db, "john")
        self.assertEqual(directors_count, 131)

    def test_input_escaping(self):
        malicious_name = "/*malicious code*/you_should_prevent_sql_injection"
        directors_count = directors_named_like_count(db, malicious_name)
        self.assertEqual(directors_count, 0)

    def test_movies_longer_than(self):
        long_movies_list = results['long_movies']
        response = movies_longer_than(db, 300)
        self.assertIs(type(response), list)
        self.assertEqual(response, long_movies_list)
