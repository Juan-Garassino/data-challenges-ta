# pylint:disable=C0111,C0103

def query_orders(db):
    """return a list of orders with displaying each column"""
    request = '''YOUR CODE HERE'''
    db.execute(request)
    results = db.fetchall()
    return results


def get_orders_range(db, date_from, date_to):
    """return a list of orders with all columns with OrderDate between
    date_from to date_to"""
    pass


def get_waiting_time(db):
    """get a list with all the orders with each column + and calculate an extra
    TimeDelta column displaying the number of days between OrderDate and
    ShippedDate ordered by ascending timedelta"""
    pass
