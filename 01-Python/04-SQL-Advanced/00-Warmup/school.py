# pylint:disable=C0111,C0103

def students_from_city(db, city):
    """return a list of students from a specific city"""
    request = '''
        SELECT *
        FROM students
        WHERE birth_city = ?
    '''
    # Use ? in your SQL query to inject the city parameter
    db.execute(request, (city,))
    results = db.fetchall()
    return results
