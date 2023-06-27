# Meal Planning Script

This Python script generates a weekly meal plan based on a dataset of recipes and their nutritional information. The goal is to create meal plans that provide more than 100% of the daily required intake of vitamins and minerals while also hitting a target calorie count and budget.

The script uses a PostgreSQL database to store the recipe data and retrieves random recipes to create a meal plan. It checks the nutritional content, calorie count, and budget of the meal plan to ensure it meets the required criteria.

## Prerequisites

- Python 3.x
- PostgreSQL database
- psycopg2 library (install using `pip install psycopg2`)

## Usage

1. Clone the repository or download the script file.

2. Ensure that the PostgreSQL database is set up and running. Update the database connection details in the script (`host`, `database`, `user`, `password`) to match your configuration.

3. Prepare the recipe data in CSV format. Each recipe should have columns for recipe name, nutritional information (vitamin A, vitamin C, iron, calories), and price. The CSV files should be stored in a specified folder.

4. Update the script to specify the folder path containing the recipe CSV files (`csv_folder` variable).

5. Run the script using the command: `python meal_planning.py`

6. The script will generate a valid meal plan based on the provided dataset and display the meal plan, nutritional content, and budget. It will also export the meal plan to a CSV file (`meal_plans.csv`).

## Customization

- Adjust the `required_intake` dictionary in the script to set your desired daily intake of vitamins, minerals, calories, and budget.

- Customize the CSV file format and structure based on your recipe data.

- Modify the code as needed to fit your specific requirements.

## License

This project is licensed under the [MIT License](LICENSE).

