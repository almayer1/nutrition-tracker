Nutrition Tracker (Python + MySQL)

A simple command-line nutrition tracker that stores foods (nutrition per 100g), lets you log what you ate by grams, and prints a daily summary (calories + macros).

What’s in this repo:

src/app.py (runs the program)

src/cli.py (menus + prompts)

src/queries.py (all database queries)

src/setup_db.py (sets up the database using the schema)

sql/schema.sql (tables/schema)

requirements.txt (Python dependencies)

Features:

Add foods to the database (calories, protein, fat, carbs, sugar per 100g)

Log foods eaten by grams for a specific date (or “today”)

View daily totals and compare to goals (if configured)

Requirements:

Python 3.9+

MySQL running

Dependencies in requirements.txt

How to run:

Install dependencies:
pip install -r requirements.txt

Create the database + tables:
python src/setup_db.py

Start the app:
python src/app.py

Notes:

MySQL connection settings (host/user/database) are set in the Python files; the password is not stored in the repo.

Keep your .venv folder out of GitHub (your .gitignore should handle it).

Author:
Alex Mayer
https://github.com/almayer1
