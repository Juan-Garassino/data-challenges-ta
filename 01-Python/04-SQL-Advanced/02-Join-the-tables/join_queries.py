# pylint:disable=missing-module-docstring

import unittest
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()


def detailed_orders(db):
    """TODO: return the list of all orders (order_id, customer.contact_name, employee.firstname) ordered by order_id"""
    request = '''SELECT orders.OrderID, customers.ContactName, employees.FirstName FROM orders
        JOIN customers ON orders.CustomerID = customers.CustomerID
        JOIN employees ON orders.EmployeeID = employees.EmployeeID
        ORDER BY orders.OrderID
    '''
    results = db.execute(request)
    results = results.fetchall()
    return results

def spent_per_customer(db):
    """TODO: return the total amount spent per customer ordered by ascending total amount (keep only 2 numbers after the ',')
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    """
    request = '''SELECT customers.ContactName,
                    ROUND(SUM(orderdetails.UnitPrice * orderdetails.Quantity), 2) AS "Total Spent"
        FROM customers
        JOIN orders ON orders.CustomerID = customers.CustomerID
        JOIN orderdetails ON orders.OrderID = orderdetails.OrderID
        GROUP BY customers.ContactName
        ORDER BY "Total Spent"
    '''
    results = db.execute(request)
    results = results.fetchall()
    return results

def best_employee(db):
    """TODO: return the first and last name of the best employee (the one who sell the most in terms of amount of money"""
    request = '''SELECT employees.FirstName, employees.LastName,
                    SUM(orderdetails.UnitPrice * orderdetails.Quantity) AS "Total Spent"
        FROM employees
        JOIN orders ON orders.EmployeeID = employees.EmployeeID
        JOIN orderdetails ON orders.OrderID = orderdetails.OrderID
        GROUP BY employees.FirstName
        ORDER BY "Total Spent" DESC
        LIMIT 1
    '''
    results = db.execute(request)
    results = results.fetchall()
    return results

def orders_per_customer(db):
    '''TO DO: return a list of tuple where each tupe contains the contactName of the customer and the number of orders he made (contactName, number_of_orders). Order the list by ascending number of orders'''
    request = '''
          SELECT customers.ContactName, count(orders.OrderID)
          FROM customers
          LEFT JOIN orders ON orders.CustomerID = customers.CustomerID
          GROUP BY orders.CustomerID
          ORDER BY count(orders.OrderID)
    '''
    results = db.execute(request)
    results = results.fetchall()
    return results

#results = detailed_orders(db)
results = orders_per_customer(db)
#results = best_employee(db)
print(type(results))
print(len(results))
print(results)
