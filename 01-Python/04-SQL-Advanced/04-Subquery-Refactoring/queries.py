# pylint:disable=C0111,C0103

def get_average_purchase(db):
    # return the average amount spent per order for each customer ordered by customer ID
    request = '''
        WITH OrderValues AS (
          SELECT
            SUM(od.UnitPrice * od.Quantity) AS value,
            od.OrderID
          FROM OrderDetails od
          GROUP BY od.OrderID
        )
        SELECT
            c.CustomerID,
            ROUND(AVG(ov.value), 2) AS average
        FROM Customers c
        JOIN Orders o ON c.CustomerID = o.CustomerID
        JOIN OrderValues ov ON ov.OrderID = o.OrderID
        GROUP BY c.CustomerID
        ORDER BY c.CustomerID
    '''
    return db.execute(request).fetchall()

def get_general_avg_order(db):
    # return the average amount spent per order
    request = '''
        WITH OrderValues AS (
          SELECT SUM(od.Quantity * od.UnitPrice) AS value
          FROM OrderDetails od
          GROUP BY od.OrderID
        )
        SELECT ROUND(AVG(ov.value), 2)
        FROM OrderValues ov
    '''
    return db.execute(request).fetchone()[0]

def best_customers(db):
    # return the customers who have an average purchase greater than the general average purchase
    request = '''
        WITH OrderValues AS (
          SELECT
            SUM(od.UnitPrice * od.Quantity) AS value,
            od.OrderID
          FROM OrderDetails od
          GROUP BY od.OrderID
        ),
        GeneralOrderValue AS (
          SELECT ROUND(AVG(ov.value), 2) AS average
          FROM OrderValues ov
        ),
        CustomerOrderValue AS (
          SELECT
            c.CustomerID,
            ROUND(AVG(ov.value), 2) AS average
          FROM Customers c
          JOIN Orders o ON c.CustomerID = o.CustomerID
          JOIN OrderValues ov ON ov.OrderID = o.OrderID
          GROUP BY c.CustomerID
          ORDER BY c.CustomerID
        )
        SELECT
            CustomerOrderValue.CustomerID,
            CustomerOrderValue.average
        FROM CustomerOrderValue
        WHERE CustomerOrderValue.average > (SELECT average FROM GeneralOrderValue)
        ORDER BY CustomerOrderValue.average DESC
    '''
    return db.execute(request).fetchall()

def top_ordered_product_per_customer(db):
    # return the list of the top ordered product by each customer based on the total ordered amount
    query = """
        WITH OrderItemAmounts AS (
            SELECT
                Orders.CustomerID,
                ProductID,
                OrderDetails.UnitPrice,
                OrderDetails.Quantity,
                SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) OrderItemAmount
            FROM Customers
            JOIN Orders ON Customers.CustomerID = Orders.CustomerID
            JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
            GROUP BY Orders.CustomerID, ProductID
        ),
        CustomerProductRanks AS (
            SELECT
                *,
                RANK() OVER(PARTITION BY CustomerID ORDER BY OrderItemAmount DESC) CustomerProductRank
            FROM OrderItemAmounts
        )
        SELECT
            CustomerID,
            ProductID,
            OrderItemAmount OrderedAmount
        FROM CustomerProductRanks
        WHERE CustomerProductRank = 1
        ORDER BY OrderedAmount DESC
    """
    return db.execute(query).fetchall()

def average_number_of_days_between_orders(db):
    # return the average number of days between two consecutive orders of the same customer
    query = """
        WITH RankedOrders AS (
            SELECT
                OrderID,
                CustomerID,
                OrderDate,
                RANK() OVER (
                    PARTITION BY CustomerID
                    ORDER BY OrderDate
                ) OrderRank
            FROM Orders
        ),
        DatedOrders AS (
            SELECT
                CustomerID,
                OrderRank,
                OrderDate,
                LAG(OrderDate, 1, 0) OVER ( PARTITION BY CustomerID ORDER BY OrderRank ) PreviousOrderDate
            FROM RankedOrders
        )
        SELECT
            ROUND(AVG(JULIANDAY(OrderDate) - JULIANDAY(PreviousOrderDate))) AVGDateDifference
        FROM DatedOrders
        WHERE PreviousOrderDate != 0
    """
    return int(db.execute(query).fetchone()[0])
