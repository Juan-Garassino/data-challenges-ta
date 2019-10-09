# pylint:disable=missing-module-docstring

import unittest
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

def first_subquery(db):
    """TO DO: ..."""
    request = '''
    TO DO
    '''
    results = db.execute(request)
    return results

results = first_subquery(db)
for r in results:
    print(r)
