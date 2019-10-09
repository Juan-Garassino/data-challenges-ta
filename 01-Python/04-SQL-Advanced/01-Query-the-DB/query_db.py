# pylint:disable=missing-module-docstring

def query_orders(db):
    """TODO: return the list of all orders with their album and artist"""
    request = '''SELECT * FROM orders'''
    results = db.execute(request)
    return results
