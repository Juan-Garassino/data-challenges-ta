# pylint:disable=missing-module-docstring
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

def query_orders(db):
    """TODO: return a list of orders with each column"""
    request = '''SELECT * FROM orders'''
    results = db.execute(request)
    return results


def get_orders_range(db, date_from, date_to):
    """TO DO: return a list of orders with each column with OrderDate between date_from to date_to"""
    t = (date_from, date_to)
    request = '''SELECT * FROM orders
    WHERE orders.OrderDate>? and orders.OrderDate<?
    '''
    results = db.execute(request, t)
    return results


def get_orders_range(db):
    """TO DO: get a list with all the orders with each column + and extra TimeDelta column displaying the number of days between OrderDate and ShippedDate orders by ascending timedelta"""
    request = '''SELECT
    *,
    julianday(orders.ShippedDate) - julianday(orders.OrderDate) AS TimeDelta
    FROM orders
    ORDER BY TimeDelta ASC
    '''
    results = db.execute(request)
    return results

date_from = "2012-01-04"
date_to = "2012-05-04"
#results = get_orders_range(db, date_from, date_to)
results = get_waiting_time(db)
results = results.fetchall()
print(results)
