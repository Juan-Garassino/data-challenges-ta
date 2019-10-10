# pylint:disable=missing-module-docstring
import unittest
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

def get_average_purchase(db):
    '''TO DO: return the average purchase per customer ordered by customer ID'''
    request = '''SELECT
                    ROUND(AVG(orderdetails.UnitPrice * orderdetails.Quantity), 2),
                    orders.CustomerID
                  FROM orders
                  JOIN orderdetails ON orders.OrderID = orderdetails.OrderID
                  GROUP BY orders.CustomerID
                  ORDER BY orders.CustomerID
              '''
    results = db.execute(request)
    results = results.fetchall()
    return results

print('--------------')
results = get_average_purchase(db)
print(results)

def get_general_avg_order(db):
    '''TO DO: return the general av'''
    request = '''SELECT
                    ROUND(AVG(orderdetails.UnitPrice * orderdetails.Quantity),2)
                  FROM orderdetails
              '''
    results = db.execute(request)
    results = results.fetchall()
    return results

print('--------------')
results = get_general_avg_order(db)
print(results)

def display_best_buyers(db):
    '''TO DO: return the customers who have an average purchase bigger than the general average purchase'''
    # It shoud return a list of tuple (average, customer_id) ordered by customer ID
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
    ORDER BY AveragePerCustomer.CustomerID
    '''
    results = db.execute(request)
    results = results.fetchall()
    return results

print('-----------------')
results = display_best_buyers(db)
print(results)

results = get_average_purchase(db)
print(results)
