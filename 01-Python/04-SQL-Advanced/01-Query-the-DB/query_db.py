# pylint:disable=missing-module-docstring

def query_orders(db):
    """TODO: return the list of all orders with their album and artist"""
    request = '''SELECT * FROM orders'''
    results = db.execute(request)
    return results


def get_orders_range(db, date_from, date_to):
    """TO DO: orders with OrderDate between date_from to date_to"""
    request = '''
    '''
    results = db.execute(request)
    return results


def get_waiting_time(db):
    """TO DO: get a list with all the orders and the timedelta between OrderDate and ShippedDate orders by ascending timedelta"""
    request = '''
    '''
    results = db.execute(request)
    return results
