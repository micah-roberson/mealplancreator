import random

# Recipe dictionary with nutritional information and price
recipes = {
    'Omelette': {'vitamin_a': 10, 'vitamin_c': 20, 'iron': 15, 'calories': 300, 'price': 2.5},
    'Salad': {'vitamin_a': 30, 'vitamin_c': 40, 'iron': 5, 'calories': 200, 'price': 3.0},
    'Smoothie': {'vitamin_a': 20, 'vitamin_c': 30, 'iron': 10, 'calories': 150, 'price': 2.0},
    # Add more recipes and their nutritional information here
}

# Required daily intake of vitamins, minerals, calories, and budget
required_intake = {'vitamin_a': 100, 'vitamin_c': 100, 'iron': 100, 'calories': 2000, 'budget': 20.0}

# Function to calculate the total nutritional content, calories, and cost of a meal plan
def calculate_nutritional_content(meal_plan):
    total_nutrition = {key: 0 for key in required_intake}
    for meal in meal_plan:
        for nutrient in meal:
            total_nutrition[nutrient] += meal[nutrient]
    return total_nutrition

# Generate a random meal plan for a week
def generate_meal_plan():
    meal_plan = []
    for _ in range(7):  # 7 days in a week
        meal = random.choice(list(recipes.keys()))
        meal_plan.append(recipes[meal])
    return meal_plan

# Check if a meal plan meets the required nutritional intake, calorie count, and budget
def is_meal_plan_valid(meal_plan):
    total_nutrition = calculate_nutritional_content(meal_plan)
    for nutrient in total_nutrition:
        if total_nutrition[nutrient] < required_intake[nutrient]:
            return False
    total_calories = total_nutrition['calories']
    if total_calories != required_intake['calories']:
        return False
    total_budget = calculate_total_budget(meal_plan)
    if total_budget > required_intake['budget']:
        return False
    return True

# Calculate the total budget of a meal plan
def calculate_total_budget(meal_plan):
    total_budget = 0
    for meal in meal_plan:
        total_budget += meal['price']
    return total_budget

# Filter recipes based on specified macro nutrients
def filter_recipes_by_macro(recipe_list, macro, min_value, max_value):
    filtered_recipes = []
    for recipe in recipe_list:
        if min_value <= recipe[macro] <= max_value:
            filtered_recipes.append(recipe)
    return filtered_recipes

# Keep generating meal plans until a valid one is found
meal_plan = generate_meal_plan()
while not is_meal_plan_valid(meal_plan):
    meal_plan = generate_meal_plan()

# Print the final meal plan and nutritional content
for i, meal in enumerate(meal_plan, 1):
    print(f"Day {i}: {list(recipes.keys())[list(recipes.values()).index(meal)]}")
print("------")
print("Total Nutritional Content:")
for nutrient, value in calculate_nutritional_content(meal_plan).items():
    print(f"{nutrient}: {value}")
print(f"Total Budget: {calculate_total_budget(meal_plan)}")

# Example: Filter recipes based on specified macro nutrients
filtered_recipes = filter_recipes_by_macro(list(recipes.values()), 'calories', 100, 250)
print("Filtered Recipes:")
for recipe in filtered_recipes:
    print(list(recipes.keys())[list(recipes.values()).index(recipe)])
