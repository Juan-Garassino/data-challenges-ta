# pylint: disable-all
import unittest
from subqueries import display_best_buyers
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

class TestBestCustomers(unittest.TestCase):
    def test_length_results(self):
        results = display_best_buyers(db)
        self.assertEqual(len(results), 3)

    def test_results(self):
        results = display_best_buyers(db)
        expected = [(572.91, 2), (870.01, 4), (548.15, 5)]
        self.assertEqual(results, expected)

    def test_type_results(self):
        results = display_best_buyers(db)
        self.assertIsInstance(results, list)
