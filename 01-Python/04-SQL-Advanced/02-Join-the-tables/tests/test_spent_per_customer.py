# pylint: disable-all
import unittest
from join_queries import spent_per_customer
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

# 1. check the type of the results
# 2. Check the first result
# 3. Check the last result
class TestSpentCustomer(unittest.TestCase):
    def check_type_results(self):
        results = spent_per_customer(db)
        results = results.fetchall()
        self.assertEqual(1, 20)

    def check_first_result(self):
        results = spent_per_customer(db)
        results = results.fetchall()
        self.assertEqual(1, 20)

    def check_last_result(self):
        results = spent_per_customer(db)
        results = results.fetchall()
        self.assertEqual(1, 20)
