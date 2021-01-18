# pylint:disable=C0111,C0103

def order_rank_per_customer(db):
    query = """
        SELECT
            OrderID,
            CustomerID,
            OrderDate,
            RANK() OVER (
                PARTITION BY CustomerID
                ORDER BY OrderDate
            ) as OrderRank
        FROM Orders
    """
    db.execute(query)
    orders = db.fetchall()
    return orders

def order_cumulative_amount_per_customer(db):
    query = """
        SELECT
            Orders.OrderID,
            Orders.CustomerID,
            Orders.OrderDate,
            SUM(SUM(OrderDetails.UnitPrice * OrderDetails.Quantity)) OVER(
                PARTITION BY Orders.CustomerID 
                ORDER BY Orders.OrderDate)
            ) as OrderCumulativeAmount
        FROM Orders
        JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
        GROUP BY Orders.OrderID
        ORDER BY Orders.CustomerID
    """
    db.execute(query)
    orders = db.fetchall()
    return orders
