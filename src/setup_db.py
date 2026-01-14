# Run seperately from app to setup the database

import mysql.connector
from mysql.connector import Error

#connects to MySQL server
def create_server_connection(host_name: str, user_name: str, user_password: str): 
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()

def execute_query(conn, query: str) -> None:
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        for _statement, _result_set in cursor.fetchsets():
            pass
        conn.commit()
    except Error as e:
        conn.rollback()
        print(f"Error: '{e}'")

def main() -> None:
    host = "localhost"
    user = "root"
    pwd = input("Enter your password: ")
    connection = create_server_connection(host, user, pwd)
    filename = "../sql/schema.sql" 
    sql_text = read_file(filename)
    execute_query(connection, sql_text)

if (__name__ == '__main__'):
    main()