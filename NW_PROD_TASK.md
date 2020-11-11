# Task
SQL OOP

    OOP task using pyodbc

An sql manager for the products table

create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.

As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department.

The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.

Create two files nw_products.py & nw_runner.py and then we will move into creating our object.

Our first requirement...
We've had a requirement for the stock department to print out the average value of all of our stock items.

Away we go....

!!!Important Note!!! It would be more efficient to write the SQL query to find the data and compute the value and simply return the value in Python.
# Solution
## nw_products file
- First we need to create a ```nw_products.py``` file and as always we'll import pyodbc to connect with the Northwind
 database
```
import pyodbc  # Importing pyodbc so that we can connect to our SQL database
``` 
- Creating our class to hold the functionality specified in the Task
```
# Our class that will handle all functionality surrounding the Products table in the NW DB
class NorthwindProducts:
```
**Connecting Method**
- First we'll define a method that handles making the connection to our database that will return a cursor so that we
 can call this method from other methods and make use of it
```
 # Method to connect to the DB, we can call this from the other methods
    def connect(self):
        # We will connect to our Northwind DB which we've already used in the SQL week
        server = "databases1.spartaglobal.academy"
        database = "Northwind"
        username = "SA"
        password = "Passw0rd2018"
        # Server name, database name, username, and password are required to connect to pyodbc
        northwind_connection = pyodbc.connect(('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                               + server + ';DATABASE=' + database + ';UID='
                                               + username + ';PWD=' + password))
        # Creating and returning a cursor to be used in the other methods
        cursor = northwind_connection.cursor()
        return cursor
```
**Product Data Method**
- The stock department sound like they'll need to interact with data from the Products table a lot
- We'll create a method that returns the contents of the table so that in the future they can use this to easily iterate
 through said data
```
    # Method to retrieve all the rows in the table, can be used to iterate through as needed
    def get_products(self):
        # Getting the cursor from the connection method and running a query to get all the data from the Products table
        cursor = self.connect()
        prod_row = cursor.execute("SELECT * FROM Products;").fetchall()
        return prod_row
```
**Average Stock Price Method**
- Now onto the requirement that the stock department specifically requested: getting the average value of all of the
 stock items
- This is easily achieved with an SQL command ```AVG(column_name)``` gets the average of all records for that column
```
    # Method that gets the average price over all products
    def avg_val(self):
        cursor = self.connect()
        average_value = cursor.execute("SELECT AVG(UnitPrice) FROM Products;").fetchone()
        return average_value
```
## nw_run file
- We'll create our ```nw_run.py``` file to run the methods we've created in ```nw_products.py```
- To have access to this functionality we'll inherit from the NorthwindProducts class, which requires us to first
 import it
```
from nw_products import NorthwindProducts  # Importing the class we want to run methods from
```
- Remember to include the name of our imported class in parentheses after our class name. This is what actually gives us
 access to the imported classes methods
```
class Runner(NorthwindProducts):
    # We only need to run the avg_val() method so lets return what's returned from the avg_val() method
    def run_avg_val(self):
        return self.avg_val()
```
- To test if this works, we can create an instance of our Runner class and call this method to see the output
```
# Creating an instance and running our method
test = Runner()
print(test.run_avg_val())
```