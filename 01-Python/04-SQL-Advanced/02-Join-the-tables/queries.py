# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    request = '''
        SELECT
            orders.OrderID,
            customers.ContactName,
            employees.FirstName
        FROM orders
        JOIN customers ON orders.CustomerID = customers.CustomerID
        JOIN employees ON orders.EmployeeID = employees.EmployeeID
    '''
    return db.execute(request).fetchall()

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    request = '''
        SELECT
            Customers.ContactName,
            SUM(details.UnitPrice * details.Quantity) AS cumulative_amount
        FROM OrderDetails AS details
        JOIN Orders ON details.OrderID = Orders.OrderId
        JOIN Customers ON Orders.CustomerID = Customers.CustomerID
        GROUP BY ContactName
        ORDER BY cumulative_amount
    '''
    return db.execute(request).fetchall()

def best_employee(db):
    '''return the first and last name of the best employee (the one
    who sells the most in terms of amount of money'''
    request = '''
        SELECT
            Employees.FirstName,
            Employees.LastName,
            SUM(details.UnitPrice * details.Quantity) AS cumulative_amount
        FROM OrderDetails AS details
        JOIN Orders ON details.OrderID = Orders.OrderID
        JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
        GROUP BY Employees.EmployeeID
        ORDER BY cumulative_amount DESC
        LIMIT 1
    '''
    return db.execute(request).fetchall()

def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    request = '''
        SELECT
            Customers.ContactName,
            COUNT(Orders.OrderID) AS order_amount
        FROM Customers
        LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
        GROUP BY Customers.CustomerID
        ORDER BY order_amount ASC
    '''
    return db.execute(request).fetchall()
