# pylint:disable=C0111,C0103

def query_orders(db):
    """TODO: return a list of orders with displaying each column"""
    request = '''YOUR CODE HERE'''
    results = db.execute(request)
    results = results.fetchall()
    return results


def get_orders_range(db, date_from, date_to):
    """TO DO: return a list of orders with each column with OrderDate between date_from to date_to"""
    pass


def get_waiting_time(db):
    """TO DO: get a list with all the orders with each column + and extra TimeDelta column displaying the number of days between OrderDate and ShippedDate orders by ascending timedelta"""
    pass
