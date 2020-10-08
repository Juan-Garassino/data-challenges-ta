# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return the list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    pass


def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (keep only 2 numbers after the ',')
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    pass


def best_employee(db):
    '''return the first and last name of the best employee (the one who sell
    the most in terms of amount of money'''
    pass


def orders_per_customer(db):
    '''return a list of tuple where each tupe contains the contactName of the
    customer and the number of orders he made (contactName, number_of_orders).
    Order the list by ascending number of orders'''
    pass
