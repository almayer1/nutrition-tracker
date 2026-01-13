import queries
from mysql.connector import Error

def main_menu(conn):
    choice = input("""
                   Please select an option
                   [1] Log Food Entry
                   [2] Daily Summary
                   [3] Add Food to Database
                   [4] List Foods in Database
                   [q] Quit
                   """)
    if choice == 1:
        prompt_log_food(conn)
        return True
    elif choice == 2:
        prompt_daily_summary(conn)
        return True
    elif choice == 3:
        prompt_add_food(conn)
        return True
    elif choice == 4:
        prompt_list_foods(conn)
        return True
    else:
        return False

def prompt_log_food(conn) -> None:
    print("Logging Entry")
    name = input("Enter the food name: ")
    grams = input("Enter the number of grams: ")
    day = input("Enter date you want to log for ('YYYY-MM-DD' or 'today'): ")
    if day == "today":
        day = None
    try:
        queries.log(conn, name, float(grams), day=day)
        print(f"Successfully logged {grams} grams of {name}")
    except ValueError as e:
        print(e)
    except Error as e:
        print(e)

def prompt_daily_summary(conn) -> None:
    pass

def prompt_add_food(conn) -> None:
    pass

def prompt_list_foods(conn) -> None:
    pass
