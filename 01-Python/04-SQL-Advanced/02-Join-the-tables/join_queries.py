# pylint:disable=missing-module-docstring

import unittest
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()


def detailed_orders(db):
    """TODO: return the list of all orders with their buyer (customer) and their seller (employee)"""
    request = '''SELECT orders.OrderID, customers.ContactName, employees.FirstName FROM orders
        JOIN customers ON orders.CustomerID = customers.CustomerID
        JOIN employees ON orders.EmployeeID = employees.EmployeeID
    '''
    results = db.execute(request)
    return results

def spent_per_customer(db):
    """TODO: return the total amount spent per customer ordered by ascending total amount
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    """
    request = '''SELECT customers.ContactName,
                    SUM(orderdetails.UnitPrice * orderdetails.Quantity) AS "Total Spent"
        FROM customers
        JOIN orders ON orders.CustomerID = customers.CustomerID
        JOIN orderdetails ON orders.OrderID = orderdetails.OrderID
        GROUP BY customers.ContactName
        ORDER BY "Total Spent"
    '''
    results = db.execute(request)
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
    return results

#results = detailed_orders(db)
#results = spent_per_customer(db)
results = best_employee(db)
results = results.fetchall()
for r in results:
    print(r)
