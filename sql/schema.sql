CREATE DATABASE IF NOT EXISTS nutrition_tracker;
USE nutrition_tracker;

CREATE TABLE IF NOT EXISTS foods(
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    calories_100g DECIMAL(4,1) NOT NULL,
    protein_100g DECIMAL(4,1),
    fat_100g DECIMAL(4,1),
    carbs_100g DECIMAL(4,1),
    sugar_100g DECIMAL(4,1)
);

CREATE TABLE IF NOT EXISTS daily_logs(
    log_id INT AUTO_INCREMENT PRIMARY KEY, 
    day DATE NOT NULL UNIQUE,
    notes VARCHAR(100),
    weight DECIMAL(4,1)
);

CREATE TABLE IF NOT EXISTS log_entries(
    id INT AUTO_INCREMENT PRIMARY KEY,
    grams_of_food DECIMAL(5,1) NOT NULL,
    food_id INT NOT NULL,
    log_id INT NOT NULL,
    FOREIGN KEY(food_id) REFERENCES foods(food_id) ON DELETE SET NULL,
    FOREIGN KEY(log_id) REFERENCES daily_logs(log_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS goals(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    calorie_goal INT NOT NULL,
    protein_goal INT ,
    fat_goal INT,
    carbs_goal INT,
    sugar_goal INT
);