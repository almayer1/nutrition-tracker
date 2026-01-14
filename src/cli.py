import queries
from mysql.connector import Error
from datetime import date

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
    #Find the log_id for today using daily_logs table. --- need a get_log_id(date) -> int: func
    day = date.today()
    log_id = queries.get_log_id(conn, day)

    #Using found log_id find food_id and grams eaten today in log_entries table --- need a get_log(conn, log_id) -> list of tuples
    foods_eaten = queries.get_log(conn, log_id)
    
    #calculate the macros consumed and name of food using food_id and grams in foods table --- get_food_macros(conn, food_id, grams) -> tuple:
    log = []
    for food in foods_eaten:
        food_id, grams = food
        log.append(queries.get_food_macros(conn, food_id, grams))

    #compare current macros with goal macros by using goals table --- get_goals(conn, user_id = 1) -> list:
    totals = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0, "sugar": 0}
    for entry in log:
        totals["calories"] += entry[1]
        totals["protein"] += entry[2]
        totals["fat"] += entry[3] 
        totals["carbs"] += entry[4] 
        totals["sugar"] += entry[5]

    goals = queries.get_goals(conn)

    #display everything
    print(f"Summary for {day}")
    print(f"Calories: {totals['calories']}/{goals[0]}")
    print(f"Protein: {totals['protein']}/{goals[1]}")
    print(f"Fat: {totals['fat']}/{goals[2]}")
    print(f"Carbohydrates: {totals['carbs']}/{goals[3]}")
    print(f"Sugar: {totals['sugar']}/{goals[4]}")

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
    print("Foods in Datbase:")
    queries.list_foods(conn)

