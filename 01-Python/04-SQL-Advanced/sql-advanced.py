import sqlite3
conn = sqlite3.connect('db/jukebox.sqlite')
c = conn.cursor()

# 0. QUICK TEST - Setup.
c.execute('''
  SELECT * FROM artists LIMIT 3
''')
print(c.fetchone())

# 1. JOINTURE


# 2. WITH


# 3. JOIN


# 4. RANK


# 5. PARTITION


