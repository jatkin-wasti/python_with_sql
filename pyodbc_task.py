# Importing pyodbc so that we can connect to our SQL database
import pyodbc


class PyodbcTask:
    # Method that will connect us to the northwind database
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
        cursor = northwind_connection.cursor()
        return cursor

    # Method that will take any number of arguments and will try to create a table using them
    def create_table(self, *args):
        i = 0
        sql_query = "CREATE TABLE"
        for _ in args:
            if i == 0:
                sql_query = sql_query + ' ' + _ + ' ('
                i += 1
            elif i % 2 != 0:
                sql_query = sql_query + '\n    ' + _ + ' '
                i += 1
            else:
                sql_query = sql_query + _ + ','
                i += 1

        # Stripping the final comma and ending the query with an ending parenthesis and semicolon
        sql_query = sql_query.rstrip(sql_query[-1]) + ');'
        # Creating our cursor and running the query we just built
        cursor = self.connect()
        cursor.execute(sql_query)

    # Method that will insert provided values into the provided table, this will only work for the Jamie_Table
    def insert(self):
        # Creating our cursor and creating our table as it seems that the table must be made in the same function as
        # the one that inserts into it (this may be a db issue)
        cursor = self.connect()
        cursor.execute("CREATE TABLE Jamie_Table (FirstName varchar(30), LastName varchar(30), Age int);")
        # Retrieving user input to add to a table
        table_name = input("Please enter the name of the table you wish to insert data into:  ")
        val1 = input("Please enter the value you'd like to input into the first column:  ")
        val2 = input("Please enter the value you'd like to input into the second column:  ")
        val3 = input("Please enter the value you'd like to input into the third column:  ")
        # Executing the query with the users inputs
        cursor.execute(f"INSERT INTO {table_name} (FirstName, LastName, Age)\n"
                       f"VALUES ('{val1}', '{val2}', {val3});")


# Creating an instance of our class to run its functionality
test = PyodbcTask()
# Testing our creating tables function
test.create_table("Jamie_Table", "FirstName", "varchar(30)", "LastName", "varchar(30)",
                                                                         "Age", "int")
# Testing our insert to tables function
test.insert()
