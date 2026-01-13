from mysql.connector import Error
from datetime import date
from typing import Optional

#creates a new food item
def add_food(conn, name: str, calories_100g: float, *, protein_100g: float = None, fat_100g: float = None, carbs_100g: float = None, sugar_100g: float = None) -> None:
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO foods (name, calories_100g, protein_100g, fat_100g, carbs_100g, sugar_100g) VALUES (%s, %s, %s, %s, %s, %s);""", (name, calories_100g, protein_100g, fat_100g, carbs_100g,sugar_100g))
        conn.commit()
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()

def list_foods(conn) -> None:
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM foods")
        row = cursor.fetchone()
        while row is not None:
            print(row,)
            row = cursor.fetchone()
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()

#updates a food based on newly passed in parameters
def update_food(conn, name:str, *, calories_100g: float = None, protein_100g: float = None, fat_100g: float = None, carbs_100g: float = None, sugar_100g: float = None):
    cursor = conn.cursor()
    try:
        id = get_food_id(conn, name)
        if id is None:
            print("Please check the name of the food you want to update and retry")
        cursor.execute(f"UPDATE foods SET calories_100g = {calories_100g}, protein_100g = {protein_100g}, fat_100g = {fat_100g}, carbs_100g = {carbs_100g}, sugar_100g = {sugar_100g} WHERE food_id = {id};")
        #FIXME - add ways to update singular attributes
        conn.commit()
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()

#delete food by name
def delete_food(conn, name: str) -> None:
    cursor = conn.cursor()
    try:
        id = get_food_id(conn, name)
        cursor.execute(f"DELETE FROM foods WHERE food_id = {id};")
        conn.commit()
    except ValueError as e:
        print(f"Error: {e}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

#converts name into id
def get_food_id(conn, name: str) -> Optional[int]:
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT food_id FROM foods WHERE name = '{name}';")
        id = cursor.fetchone()
        if id is None:
            raise ValueError(f"Food not found: {name}")
        return id[0]
    finally:
        cursor.close()

def get_log_id(conn, day: date) -> int:
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT log_id FROM daily_logs WHERE day = %s;", (day,))
        row = cursor.fetchone()
        if row is None:
            return create_log(conn, day) 
        return row[0]
    except Error as e:
        raise
    finally: 
        cursor.close()

#makes a new log for the day... day format = 'YYYY-MM-DD', returns the log_id
def create_log(conn, day, *, weight: float = None, notes: str = None) -> int:
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO daily_logs (day, weight, notes) VALUES (%s, %s, %s);", (day, weight, notes))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        conn.rollback()
        raise
    finally:
        cursor.close()
#logs food using name and grams
def log(conn, name: str, grams: float, *, day: date = None) -> None: 
    cursor = conn.cursor()
    try:
        if day is None:
            day = date.today()
        else:
            day = date.fromisoformat(day)
        food_id = get_food_id(conn, name)
        log_id = get_log_id(conn, day)
        cursor.execute("INSERT INTO log_entries (grams_of_food, log_id, food_id) VALUES (%s, %s, %s);", (grams, log_id, food_id))
        conn.commit()
    except ValueError as e:
        raise
    except Error as e:
        raise
    finally:
        cursor.close()

def list_log_entries(conn) -> None:
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM log_entries")
        row = cursor.fetchone()
        while row is not None:
            print(row,)
            row = cursor.fetchone()
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()

def list_daily_logs(conn) -> None:
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM daily_logs")
        row = cursor.fetchone()
        while row is not None:
            print(row,)
            row = cursor.fetchone()
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()