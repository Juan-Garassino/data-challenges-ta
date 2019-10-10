# pylint:disable=missing-module-docstring

import unittest
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

def group_by_customer(db):
    """TO DO: ..."""
    request = '''SELECT orders.CustomerID,
        AVG(orderdetails.UnitPrice * orderdetails.Quantity) AS AvgOrderAmount,
        MIN(orderdetails.UnitPrice * orderdetails.Quantity) AS MinOrderAmount,
        MAX(orderdetails.UnitPrice * orderdetails.Quantity) AS MaxOrderAmount,
        SUM(orderdetails.UnitPrice * orderdetails.Quantity) AS TotalOrderAmount
        FROM orders
        JOIN orderdetails ON orders.OrderID = orderdetails.OrderID
        GROUP BY orders.CustomerID
    '''
    results = db.execute(request)
    return results

def partition_by_customer(db):
    """TO DO: ..."""
    request = '''SELECT orders.CustomerID,
        orderdetails.UnitPrice * orderdetails.Quantity AS OrderAmount,
        RANK() OVER(PARTITION BY orders.CustomerID
        ORDER BY (orderdetails.UnitPrice * orderdetails.Quantity) DESC) AS "Row Number",
        orderdetails.UnitPrice,
        orderdetails.Quantity
        FROM orders
        JOIN orderdetails ON orders.OrderID = orderdetails.OrderID
    '''
    results = db.execute(request)
    return results



# results = group_by_employee(db)
results = rank_products(db)
# results = rank_orders(db)
# results = partition_by_employee(db)
# results = results.fetchall()
for r in results:
    print(r)
