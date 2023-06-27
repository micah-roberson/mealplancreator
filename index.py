import random
import csv
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a cursor to execute SQL queries
cur = conn.cursor()

# Required daily intake ranges of vitamins, minerals, calories, and budget
required_intake = {
    'vitamin_a': (700, 900),
    'vitamin_c': (75, 90),
    'vitamin_d': (600, 800),
    'vitamin_e': (15, 15),
    'vitamin_k': (90, 120),
    'thiamin': (1.1, 1.4),
    'riboflavin': (1.1, 1.3),
    'niacin': (14, 16),
    'pantothenic_acid': (100, 100),
    'vitamin_b6': (1.3, 1.7),
    'biotin': (30, 30),
    'folate': (400, 800),
    'vitamin_b12': (2.4, 2.4),
    'choline': (425, 550),
    'calcium': (1000, 1300),
    'sulfur': (100, 100),
    'phosphorus': (700, 700),
    'magnesium': (310, 420),
    'sodium': (0, 2300),
    'potassium': (4700, 4700),
    'iron': (8, 18),
    'zinc': (8, 11)
}

# Function to load recipe data from CSV files
def load_recipe_data(csv_folder):
    recipes = []
    # Iterate through each CSV file in the specified folder
    for filename in csv_folder:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            # Read each row in the CSV file and append it to the recipes list
            for row in reader:
                recipes.append(row)
    return recipes

# Generate a random meal plan for a week
def generate_meal_plan(recipes):
    meal_plan = random.sample(recipes, 7)  # Select 7 random recipes from the loaded recipes
    return meal_plan

# Check if a meal plan meets the required nutritional intake, calorie count, and budget
def is_meal_plan_valid(meal_plan, total_nutrition, total_budget):
    for meal in meal_plan:
        for nutrient, value in meal.items():
            if nutrient in total_nutrition:
                total_nutrition[nutrient] += float(value)
    return (
        all(required_intake[nutrient][0] <= total_nutrition[nutrient] <= required_intake[nutrient][1] for nutrient in total_nutrition) and
        total_nutrition['calories'] == required_intake['calories'] and
        total_budget <= required_intake['budget']
    )

# Calculate the total budget of a meal plan
def calculate_total_budget(meal_plan):
    return sum(float(meal['price']) for meal in meal_plan)

# Specify the folder path containing the CSV files
csv_folder = 'path/to/csv/folder'

# Load recipe data from the CSV files
recipes = load_recipe_data(csv_folder)

# Keep generating meal plans until a valid one is found
meal_plan = generate_meal_plan(recipes)
total_nutrition = {key: 0 for key in required_intake}
total_budget = calculate_total_budget(meal_plan)
while not is_meal_plan_valid(meal_plan, total_nutrition, total_budget):
    meal_plan = generate_meal_plan(recipes)
    total_nutrition = {key: 0 for key in required_intake}
    total_budget = calculate_total_budget(meal_plan)

# Print the final meal plan and nutritional content
for i, meal in enumerate(meal_plan, 1):
    print(f"Day {i}: {meal['recipe_name']}")
print("------")
print("Total Nutritional Content:")
for nutrient, value in total_nutrition.items():
    print(f"{nutrient}: {value}")
print(f"Total Budget: {total_budget}")

# Export the meal plan to a CSV file
with open('meal_plan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Day', 'Recipe Name'])
    for i, meal in enumerate(meal_plan, 1):
        writer.writerow([f"Day {i}", meal['recipe_name']])

# Close the database connection
cur.close()
conn.close()

