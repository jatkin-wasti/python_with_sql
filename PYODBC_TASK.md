# Task:
- Create a new file and a class with function to establish connection with pyodbc
- Create a function that creates a table in the Db
- Create a function that prompts the user to input data in that table
- Create a new file called PYODBC_TASK.md and document the steps to implement the task
# Solution
**Importing**
- As always, we need to import pyodbc to be able to interface with our SQL database
```
# Importing pyodbc so that we can connect to our SQL database
import pyodbc
```
**Connectivity Method**
- We'll create our class and define a method that handles making the connection to our database
- It will return a cursor so that we can call this method from other methods and make use of it
```
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
```
**Create Table Method**
- We want to make a method that will create a table in our database, but we don't know how many columns the user will
 want to add. So we'll use *args to allow any number of arguments and loop through them to construct our query 
```
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
```
- Adding the comma at the end works wonderfully when we're adding more columns, but once we run out of arguments it
 isn't needed and will cause an error if we leave it in. We'll use the rstrip() method to remove the right most
  character before ending the query with a closing parenthesis and semicolon
```
        # Stripping the final comma and ending the query with an ending parenthesis and semicolon
        sql_query = sql_query.rstrip(sql_query[-1]) + ');'
```
- Now that our query is constructed, we can cann our connect method and use the cursor to execute it
```
 # Creating our cursor and running the query we just built
        cursor = self.connect()
        cursor.execute(sql_query)
```
**Inserting User Input Into A Table**
- This may have been because of DB issues on the day of creation, however the methods were throwing errors when the
 table being inserted into wasn't created in the method doing the insertion. So that's the way it has been
  implemented here
```
# Method that will insert provided values into the provided table, this will only work for the Jamie_Table
    def insert(self):
        # Creating our cursor and creating our table as it seems that the table must be made in the same function as
        # the one that inserts into it (this may be a db issue)
        cursor = self.connect()
        cursor.execute("CREATE TABLE Jamie_Table (FirstName varchar(30), LastName varchar(30), Age int);")
```
- Retrieving the user's input for the three columns in our table and executing the insert with these values
```
        # Retrieving user input to add to a table
        table_name = input("Please enter the name of the table you wish to insert data into:  ")
        val1 = input("Please enter the value you'd like to input into the first column:  ")
        val2 = input("Please enter the value you'd like to input into the second column:  ")
        val3 = input("Please enter the value you'd like to input into the third column:  ")
        # Executing the query with the users inputs
        cursor.execute(f"INSERT INTO {table_name} (FirstName, LastName, Age)\n"
                       f"VALUES ('{val1}', '{val2}', {val3});")

```
- As an increment, this could be expanded to add to any table, but currently this only works for inputting data into the
 hardcoded table
 **Basic Testing Of Our Class**
- Creating an instance of the class
```
# Creating an instance of our class to run its functionality
test = PyodbcTask()
```
- Running our create_table method with the table name and the  column names and their associated data types
```
# Testing our creating tables function
test.create_table("Jamie_Table", "FirstName", "varchar(30)", "LastName", "varchar(30)",
                                                                      "Age", "int")
```
- Running our insert method and inputting data to see if it throws an error
```
# Testing our insert to tables function
test.insert()
``` 
- None of them throw an error, but this does not mean that our code is perfect!
- There are definitely inputs we can provide that will throw errors, for example: What if we tried to create a column
 without a datatype, or input something that broke the SQL syntax? What would happen if we tried to input the wrong
  data type during insertion?
- These are the things you should look out for, and are the perfect things to try to fix in the next iteration