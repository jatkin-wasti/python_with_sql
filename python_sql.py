# This will cover connecting to our SQL DB from Python using PYODBC
import pyodbc


# pyodbc driver from microsoft helps us to connect to SQL instance
# We will connect to our Northwind DB which we've already used in the SQL week
server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
# Server name, database name, username, and password are required to connect to pyodbc
northwind_connection = pyodbc.connect(('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                       + server + ';DATABASE=' + database+';UID='+username+';PWD=' + password))

# Cursor is location of your mouse/current path
cursor = northwind_connection.cursor()
# Selecting version of the DB
cursor.execute("SELECT @@VERSION")
row = cursor.fetchone()
print(row)

# In our DB we have a table called 'Customers' that holds data on customers
# Using fetchall() method we get all of the data available inside our Customers table.
cust_row = cursor.execute("SELECT * FROM Customers;").fetchall()
for records in cust_row:
    print(records)

# We have another table in the DB called Products
# Running queries in our python program to access database and the Product inside the DB
prod_row = cursor.execute("SELECT * FROM Products;").fetchall()
# Iterating through the table data and finding the UnitPrice attribute
for records in prod_row:
    print(records.UnitPrice)

# Iterating through the data until the last line of the data (until condition is False
prod_row = cursor.execute("SELECT * FROM Products;")
# Combination of our loop and control flow to ensure that we only iterate through the data as long as the data is
# available
while True:
    records = prod_row.fetchone()
    if records is None:  # When there are no records left (value is None) then stop
        break
    print(records.UnitPrice)
