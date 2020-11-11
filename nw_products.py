import pyodbc  # Importing pyodbc so that we can connect to our SQL database


# Our class that will handle all functionality surrounding the Products table in the NW DB
class NorthwindProducts:
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

    # Method to retrieve all the rows in the table, can be used to iterate through as needed
    def get_products(self):
        # Getting the cursor from the connection method and running a query to get all the data from the Products table
        cursor = self.connect()
        prod_row = cursor.execute("SELECT * FROM Products;").fetchall()
        return prod_row

    # Method that gets the average price over all products
    def avg_val(self):
        cursor = self.connect()
        average_value = cursor.execute("SELECT AVG(UnitPrice) FROM Products;").fetchone()
        return average_value


# Creating an instance of our class and testing if it runs without errors and outputs the correct values
# test = NorthwindProducts()
# test.get_products()
# print(test.avg_val())
