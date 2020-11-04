import pymssql
import time

print('Waiting 10s to SQLServer')
time.sleep(30)
print('10 seconds waited. Starting...')

conn = pymssql.connect(server="sql-server", port="1433", user="sa", password="Password1234!")

conn.autocommit(True)

cursor = conn.cursor()

# Creating database
cursor.execute("""
IF NOT EXISTS (
   SELECT name
   FROM sys.databases
   WHERE name = 'testjondb'
)
CREATE DATABASE testjondb
""")

# Use custom database
cursor.execute('USE testjondb')

conn.autocommit(False)

# Creating table
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)""")

# Inserting values on table
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()

# Selecting 
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()
mssql.
conn.close()