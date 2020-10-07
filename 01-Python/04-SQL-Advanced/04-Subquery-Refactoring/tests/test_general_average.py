# pylint: disable-all
import unittest
from subqueries import get_general_avg_order
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()


class TestGeneralAverage(unittest.TestCase):
    def test_length_results(self):
        results = get_general_avg_order(db)
        self.assertEqual(len(results), 1)

    def test_results(self):
        results = get_general_avg_order(db)
        expected = 418.48
        self.assertEqual(results, expected)

    def test_type_results(self):
        results = get_general_avg_order(db)
        self.assertIsInstance(results, list)
