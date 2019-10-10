# pylint: disable-all
import unittest
from query import *
import sqlite3

conn = sqlite3.connect('db/movies.db')
db = conn.cursor()

class TestQuery(unittest.TestCase):
    def test_length_list(self):
        self.assertEqual(0, 1)
