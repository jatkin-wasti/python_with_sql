import pyodbc


class PyodbcTask:
    def connect(self):
        # We will connect to our Northwind DB which we've already used in the SQL week
        server = "databases1.spartaglobal.academy"
        database = "Northwind"
        username = "**"
        password = "********"
        # Server name, database name, username, and password are required to connect to pyodbc
        northwind_connection = pyodbc.connect(('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                               + server + ';DATABASE=' + database + ';UID='
                                               + username + ';PWD=' + password))
        return northwind_connection

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

        sql_query = sql_query.rstrip(sql_query[-1]) + ');'
        cursor = self.connect()
        cursor.execute(sql_query)

    def add_to_table(self, table_name):
        pass
        # cursor = self.northwind_connection.cursor()
        # cursor.execute(f"INSERT INTO {table_name} ()")


test = PyodbcTask()
test.create_table("Jamie_Table", "FirstName", "varchar(30)", "LastName", "varchar(30)",
                                                                         "Age", "int")
