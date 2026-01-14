import mysql.connector
from mysql.connector import Error
from cli import main_menu

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def main() -> None:
    #create connection to database
    host = "localhost"
    user = "root"
    db = "nutrition_tracker"
    pwd = input("What is your password? ")
    connection = create_db_connection(host, user, pwd, db)
    is_running = main_menu(connection)
    while (is_running):
        is_running = main_menu(connection)
    
if __name__ == "__main__":
    main()