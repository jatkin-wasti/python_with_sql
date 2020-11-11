# Python with SQL
![Python and SQL](SQL_diagram.PNG)
## Using PYODBC to connect to SQL from our python program
- Python Open Database Connectivity
- Open source python module that lets us simply access an ODBC database
### What is a Cursor and how to use it
**What is a Cursor?**
- It is a temporary memory station allocated by the DB Server when performing DML operations on a Table

**Implicit Cursors**
- Allocated by SQL server when the user performs DML operations

**Explicit Cursors**
- Created by the user when needed
- Used for fetching data from a table in a row by row manner

#### Using cursors in Python
- cursor lets us execute queries and return the results we're loooking for
- fetchone() selects one row at a time
- fetchall() selects all rows

#### Using Explicit Cursors in SQL
- Syntax for declaring a cursor in SQL
```
DECLARE cursor_name CURSOR
    FOR select_statement_here;
```
- After creating the Cursor we have to open it
```
OPEN cursor_name;
```
- We can then use ```FETCH``` to fetch a row from the cursor and put that information into a variable
- FETCH uses the following 6 methods:
- ```FIRST```  Used to fetch only the first row from the cursor table
- ```LAST```   Used to fetch only the last row from the cursor table
- ```NEXT```   Used to fetch data in a forward direction from the cursor table
- ```PRIOR```  Used to fetch data in a backwards direction from the cursor table
- ```ABSOLUTE n``` Used to fetch the exact nth row from cursor table
- ```RELATIVE n``` Used to fetch the data in an incremental way as well as decremental way
- An example of a using one of these FETCH methods would be
```
FETCH NEXT FROM cursor INTO variable_list;
```
- We can use the ```@@FETCHSTATUS``` function to return the status of the last cursor ```FETCH``` statement executed
 against the cursor. If it returns 0 then the ```FETCH``` statement was successful
- We can use this with a ```WHILE``` loop to ```FETCH``` all the rows from the code
```
WHILE @@FETCH_STATUS = 0
    BEGIN
        FETCH NEXT FROM cursor_name;
    END;
```
- When we're done we can close the cursor
```
CLOSE cursor_name;
```
- And finally we deallocate the cursor
```
DEALLOCATE cursor_name;
```
#### Using explicit cursors in python
- 
#### Some functions that we can use to interact with SQL data

## Setting up our pyodbc connection
**Before you do anything, make sure you've downloaded a pyodbc driver. You can download it from the following link**
```
https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
```
- Command to install pyodbc
```
pip install pyodbc in pycharm
```
- Once installed, create a python_sql.py file
- Of course to use our newly installed module we'll have to import it in our file
```
import pyodbc
```
- Establish your connection to the Database
```
# pyodbc driver from microsoft helps us to connect to SQL instance
# We will connect to our Northwind DB which we've already used in the SQL week
server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "**"
password = "************"
# Server name, database name, username, and password are required to connect to pyodbc
northwind_connection = pyodbc.connect(('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                       + server + ';DATABASE=' + database+';UID='+username+';PWD=' + password)
```
- Verify the connection
```
cursor = northwind_connection.cursor()
# Selecting version of the DB
cursor.execute("SELECT @@VERSION")
row = cursor.fetchone()
print(row)
```
### Running queries to the database from our python file
- Running a query to the database, fetching all of the data from the Customers table and printing each row found
```
# In our DB we have a table called 'Customers' that holds data on customers
# Using fetchall() method we get all of the data available inside our Customers table.
cust_row = cursor.execute("SELECT * FROM Customers;").fetchall()
for records in cust_row:
    print(records)
```
- Running another query, this time getting data out of our Products table and outputting the UnitPrice stored in each
 record
```
# We have another table in the DB called Products
# Running queries in our python program to access database and the Product inside the DB
prod_row = cursor.execute("SELECT * FROM Products;").fetchall()
# Iterating through the table data and finding the UnitPrice attribute
for records in prod_row:
    print(records.UnitPrice)
```
- Running a query to perform the same task as before, but using a while loop that continues outputting until there
 aren't any records left
```
# Iterating through the data until the last line of the data (until condition is False
prod_row = cursor.execute("SELECT * FROM Products;")
# Combination of our loop and control flow to ensure that we only iterate through the data as long as the data is
# available
while True:
    records = prod_row.fetchone()
    if records is None:  # When there are no records left (value is None) then stop
        break
    print(records.UnitPrice)
```