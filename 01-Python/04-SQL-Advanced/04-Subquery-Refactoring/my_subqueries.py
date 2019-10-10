# pylint:disable=missing-module-docstring

import unittest
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

def get_average_purchase(db):
    '''TO DO: return the average purchase per customer'''
    request = '''SELECT
                    ROUND(AVG(orderdetails.UnitPrice * orderdetails.Quantity), 2),
                    orders.CustomerID
                  FROM orders
                  JOIN orderdetails ON orders.OrderID = orderdetails.OrderID
                  GROUP BY orders.CustomerID
              '''
    results = db.execute(request)
    return results

print('--------------')
results = get_average_purchase(db)
results = results.fetchall()
print(results)

def get_general_avg_order(db):
    '''TO DO: return the general av'''
    request = '''SELECT
                    ROUND(AVG(orderdetails.UnitPrice * orderdetails.Quantity),2)
                  FROM orderdetails
              '''
    results = db.execute(request)
    return results

print('--------------')
results = get_general_avg_order(db)
results = results.fetchall()
print(results)

def display_new_columns(db):
    request = '''
    WITH
        AveragePerCustomer(avg, CustomerID) AS(
            SELECT
                ROUND(AVG(orderdetails.UnitPrice * orderdetails.Quantity),2),
                orders.CustomerID
            FROM orders
            JOIN orderdetails ON orders.OrderID = orderdetails.OrderID
            GROUP BY orders.CustomerID
        ),
        GeneralAverage(genavg) AS(
            SELECT
                ROUND(AVG(orderdetails.UnitPrice * orderdetails.Quantity), 2)
            FROM orderdetails
        )
    SELECT AveragePerCustomer.avg, AveragePerCustomer.CustomerID
    FROM AveragePerCustomer, GeneralAverage
    WHERE AveragePerCustomer.avg > GeneralAverage.genavg
    '''
    results = db.execute(request)
    results = results.fetchall()
    return results

print('-----------------')
results = display_new_columns(db)
results = results.fetchall()
print(results)

