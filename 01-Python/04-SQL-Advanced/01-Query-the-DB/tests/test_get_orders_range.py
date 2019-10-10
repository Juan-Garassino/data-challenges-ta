# pylint: disable-all
import unittest
from query_db import get_orders_range
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

# 1. Test column name : TO DO
# 2. Test type(results = list) : TO DO
# 3. Good results between 2012-01-04 and 2012-03-04 : TO DO
# 4. Good results between 2012-03-15 and 2012-04-15 : TO DO
class TestOrdersRange(unittest.TestCase):
    def test_column_name(self):
        date_from = "2012-01-04"
        date_to = "2012-03-04"
        results = get_orders_range(db, date_from, date_to)
        results = results.fetchall()
        self.assertEqual(1, 2)

    def test_type_results(self):
        date_from = "2012-01-04"
        date_to = "2012-03-04"
        results = get_orders_range(db, date_from, date_to)
        results = results.fetchall()
        self.assertEqual(1, 2)

    def test_results_1(self):
        date_from = "2012-01-04"
        date_to = "2012-03-04"
        results = get_orders_range(db, date_from, date_to)
        results = results.fetchall()
        self.assertEqual(1, 2)

    def test_results_2(self):
        date_from = "2012-03-15"
        date_to = "2012-04-15"
        results = get_orders_range(db, date_from, date_to)
        results = results.fetchall()
        self.assertEqual(1, 2)

