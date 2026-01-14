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
    if choice == "1":
        prompt_log_food(conn)
        return True
    elif choice == "2":
        prompt_daily_summary(conn)
        return True
    elif choice == "3":
        prompt_add_food(conn)
        return True
    elif choice == "4":
        prompt_list_foods(conn)
        return True
    else:
        print("Exiting...")
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
    print("Today's Summary:")
    queries.list_log_entries(conn)
    

def prompt_add_food(conn) -> None:
    name = input("Enter the name of the food you want to add: ")
    calories = input("Amount of calories per 100 grams: ")
    protein = input("Amount of protein per 100 grams: ")
    fat = input("Amount of fat per 100 grams: ")
    carbs = input("Amount of carbs per 100 grams: ")
    sugar = input("Amount of sugar per 100 grams: ")
    try:
        queries.add_food(conn, name, calories, protein_100g=protein, fat_100g=fat, carbs_100g=carbs, sugar_100g=sugar)
        print(f"Successfully added {name}")
    except Error as e:
        print(e)

def prompt_list_foods(conn) -> None:
    print("Food in Datbase:")
    queries.list_foods(conn)

