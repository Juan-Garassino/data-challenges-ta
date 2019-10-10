# pylint: disable-all
import unittest
from query_db import get_orders_range
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

# 1. Test size list : TO DO
# 2. Test column name : TO DO
# 3. Test type(results = list) : TO DO
# 4. Good results first results : TO DO
# 5. Good results second results : TO DO
class TestWaitingTime(unittest.TestCase):
    def test_size_list(self):
        results = get_orders_range(db)
        results = results.fetchall()
        self.assertEqual(1, 2)

    def test_column_name(self):
        results = get_orders_range(db)
        results = results.fetchall()
        self.assertEqual(1, 2)

    def test_type_results(self):
        results = get_orders_range(db)
        results = results.fetchall()
        self.assertEqual(1, 2)

    def test_first_result(self):
        results = get_orders_range(db)
        results = results.fetchall()
        self.assertEqual(1, 2)

    def test_second_result(self):
        results = get_orders_range(db)
        results = results.fetchall()
        self.assertEqual(1, 2)
