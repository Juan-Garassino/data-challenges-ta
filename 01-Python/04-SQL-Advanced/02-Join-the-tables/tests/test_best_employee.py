# pylint: disable-all
import unittest
from join_queries import best_employee
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

# 1. Return just one element
# 2. Return the good result
# 3. Return the good type(result)
class TestBestEmployee(unittest.TestCase):
    def test_length_results(self):
        results = best_employee(db)
        results = results.fetchall()
        self.assertEqual(1, 20)

    def test_good_result(self):
        results = best_employee(db)
        results = results.fetchall()
        self.assertEqual(1, 20)

    def test_type_result(self):
        results = best_employee(db)
        results = results.fetchall()
        self.assertEqual(1, 20)
