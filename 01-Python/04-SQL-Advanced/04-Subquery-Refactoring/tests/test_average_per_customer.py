# pylint: disable-all
import unittest
from subqueries import get_average_purchase
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

class TestAveragePerCustomer(unittest.TestCase):
    def test_length_results(self):
        results = get_average_purchase(db)
        self.assertEqual(len(results), 5)

    def test_results(self):
        results = get_average_purchase(db)
        expected = [(288.81, 1), (572.91, 2), (93.99, 3), (870.01, 4), (548.15, 5)]
        self.assertEqual(results, expected)

    def test_type_results(self):
        results = get_average_purchase(db)
        self.assertIsInstance(results, list)
