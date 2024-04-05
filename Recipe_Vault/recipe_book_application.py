'''
Ian Duggan
CS 5001 Final Project
Fall Semester 2023
Digital Recipe Book Application
'''
import json
import random

# File Path
filename = 'recipes.json'

# 1. Utility Functions
def load_recipes_from_json():
    """ Load recipes from a JSON file.

    This function attempts to open and read a JSON file specified by the global variable 'filename'.
    If the file is found, it returns the contents as a dictionary.
    If the file is not found, it returns an empty dictionary.

    Returns:
        dict: The content of the JSON file as a dictionary, or an empty dictionary if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_recipes_to_json(recipes):
    """ Save recipes to a JSON file.

    This function writes the recipes dictionary to a JSON file specified by the global variable 'filename'.
    The JSON file is formatted with an indentation of 4 spaces for readability.

    Parameters:
        recipes (dict): The recipes dictionary to be saved to the JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(recipes, file, indent=4)

def view_recipes(recipes):
    """Display all recipes categorized by meat type and course type.
        
        Parameters:
            recipes (dict): A dictionary containing nested dictionaries of recipes.
    """
    if 'savory' not in recipes: # Ensure the 'savory' key exists in the recipes dictionary
        print("No savory recipes available.")
        return

    for meat_type, courses in recipes['savory'].items():
        print(f"\n{meat_type.title()}:")
        for course_type, course_details in courses['course'].items():
            print(f"  {course_type.title()}:")
            for recipe_name, recipe_details in course_details['recipes'].items():
                print(f"    - {recipe_name} (Prep Time: {recipe_details['prep time']} mins, Page: {recipe_details['page']})")

# 2. Core Functionalities
def add_recipe(recipes):
    """ 
    Add a new recipe to the recipes dictionary based on user input.
    
    Parameters:
        recipes (dict): The main recipes dictionary where the new recipe will be added.
    """
    # Display meat types and get user selection
    meat_types = list(recipes['savory'].keys())
    print("\nSelect a Meat Type:")
    for i, meat in enumerate(meat_types, 1):
        print(f"{i}. {meat.title()}")

    # Display meat types and get user selection
    while True:
        try:
            meat_choice = int(input("Enter your choice (number): ")) - 1
            if 0 <= meat_choice < len(meat_types):
                selected_meat_type = meat_types[meat_choice]
                break
            else:
                print("Please enter a number within the valid range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Display course types and get user selection
    course_types = list(recipes['savory'][selected_meat_type]['course'].keys())
    print("\nSelect a Course Type:")
    for i, course in enumerate(course_types, 1):
        print(f"{i}. {course.title()}")

    while True:
        try:
            course_choice = int(input("Enter your choice (number): ")) - 1
            if 0 <= course_choice < len(course_types):
                selected_course_type = course_types[course_choice]
                break
            else:
                print("Please enter a number within the valid range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Promot user for recipe specifics
    recipe_name = input("Enter recipe name: ")
    prep_time = int(input("Enter preparation time (in minutes): "))
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    amounts = input("Enter amounts for each ingredient (comma-separated): ").split(',')
    page = int(input("Enter page number: "))

    # Adding the new recipe
    if selected_course_type not in recipes['savory'][selected_meat_type]['course']:
        recipes['savory'][selected_meat_type]['course'][selected_course_type] = {'recipes': {}}

    recipes['savory'][selected_meat_type]['course'][selected_course_type]['recipes'][recipe_name] = {
        "prep time": prep_time,
        "ingredients": ingredients,
        "amount": amounts,
        "page": page
    }

def edit_recipe(recipes):
    """ Edit an existing recipe in the recipes dictionary based on user input.

    Parameters:
        recipes (dict): The main recipes dictionary where recipes can be edited.
    """
    #Display options to user and get user selections
    meat_type = input("Enter meat type (chicken, beef, meatless) of the recipe to edit: ")
    course_type = input("Enter course type (e.g., appetizer, entree) of the recipe to edit: ")
    recipe_name = input("Enter the name of the recipe to edit: ")

    # Prompt user for recipe edits
    if meat_type in recipes['savory'] and course_type in recipes['savory'][meat_type]['course']:
        if recipe_name in recipes['savory'][meat_type]['course'][course_type]['recipes']:
            print("Enter new details for the recipe:")
            recipes['savory'][meat_type]['course'][course_type]['recipes'][recipe_name]['prep time'] = int(input("Preparation time (minutes): "))
            recipes['savory'][meat_type]['course'][course_type]['recipes'][recipe_name]['ingredients'] = input("Ingredients (comma-separated): ").split(',')
            recipes['savory'][meat_type]['course'][course_type]['recipes'][recipe_name]['amount'] = input("Amounts (comma-separated): ").split(',')
            recipes['savory'][meat_type]['course'][course_type]['recipes'][recipe_name]['page'] = int(input("Page number: "))
        else:
            print("Recipe not found.")
    else:
        print("Meat type or course type not found.")

def delete_recipe(recipes):
    """ Delete a recipe from the recipes dictionary based on user input.

    Parameters:
        recipes (dict): The main recipes dictionary from which recipes can be deleted.
    """

    #Display options to user and get selections
    meat_type = input("Enter meat type (chicken, beef, meatless) of the recipe to delete: ")
    course_type = input("Enter course type (e.g., appetizer, entree) of the recipe to delete: ")
    recipe_name = input("Enter the name of the recipe to delete: ")

    # Delete recipe
    if meat_type in recipes['savory'] and course_type in recipes['savory'][meat_type]['course']:
        if recipe_name in recipes['savory'][meat_type]['course'][course_type]['recipes']:
            del recipes['savory'][meat_type]['course'][course_type]['recipes'][recipe_name]
            print(f"Recipe '{recipe_name}' deleted.")
        else:
            print("Recipe not found.")
    else:
        print("Meat type or course type not found.")

def select_recipe_randomly(recipes):
    """
    Selects a recipe randomly from the entire collection of recipes.

    Parameters:
    recipes (dict): The main recipes dictionary to select from.

    Returns:
    str: The name of the randomly selected recipe.
    """
    # Call recipe options
    all_recipes = []
    for meat_type, courses in recipes['savory'].items():
        for course_type, course_details in courses['course'].items():
            all_recipes.extend(course_details['recipes'].keys())

    # Select recipe at random
    if all_recipes:
        return random.choice(all_recipes)
    else:
        return "No recipes available."

def select_recipe_by_criteria(recipes):
    """
    Selects a recipe based on user-selected meat type and/or course type.
    
    The function displays available meat types and course types and allows the user to make selections
    by inputting corresponding numbers.

    Parameters:
    recipes (dict): The main recipes dictionary to select from.

    Returns:
    str: The name of the selected recipe or a message if no recipes are found.
    """

    # Display meat types and get user selection
    meat_types = list(recipes['savory'].keys())
    print("\nSelect a Meat Type:")
    for i, meat in enumerate(meat_types, 1):
        print(f"{i}. {meat.title()}")

    #Validate user input
    while True:
        try:
            meat_choice = int(input("Enter your choice (number): ")) - 1
            if 0 <= meat_choice < len(meat_types):
                selected_meat_type = meat_types[meat_choice]
                break
            else:
                print("Please enter a number within the valid range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Display course types and get user selection
    course_types = list(recipes['savory'][selected_meat_type]['course'].keys())
    print("\nSelect a Course Type:")
    for i, course in enumerate(course_types, 1):
        print(f"{i}. {course.title()}")

    #Validate user input
    while True:
        try:
            course_choice = int(input("Enter your choice (number): ")) - 1
            if 0 <= course_choice < len(course_types):
                selected_course_type = course_types[course_choice]
                break
            else:
                print("Please enter a number within the valid range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Select a recipe
    selected_recipes = list(recipes['savory'][selected_meat_type]['course'][selected_course_type]['recipes'].keys())
    if selected_recipes:
        recipe_choice = random.choice(selected_recipes)
        return recipe_choice
    else:
        return "No recipes found for the given criteria."

def generate_grocery_list(recipes, recipe_names):
    """ Generate a grocery list based on the ingredients of the selected recipes.

    Parameters:
        recipes (dict): The main recipes dictionary to reference for ingredients.
        recipe_names (list): A list of recipe names for which the grocery list is to be generated.

    Returns:
        dict: A dictionary with ingredients as keys and a list of amounts as values.
    """
    # Create empty list, and then loop through recipes to pull required ingredients
    grocery_list = {}
    for name in recipe_names:
        for meat_type, courses in recipes['savory'].items():
            for course_type, course_details in courses['course'].items():
                if name in course_details['recipes']:
                    recipe = course_details['recipes'][name]
                    for ingredient, amount in zip(recipe['ingredients'], recipe['amount']):
                        if ingredient in grocery_list:
                            grocery_list[ingredient].append(amount)
                        else:
                            grocery_list[ingredient] = [amount]
    return grocery_list

def generate_meal_plan(recipes):
    """
    Generates a weekly meal plan by randomly selecting 5 entree recipes.

    Parameters:
    recipes (dict): The main recipes dictionary from which to randomly select recipes.

    Returns:
    list: A list of the names of the selected entree recipes.
    """
    # Create empty list to add meal plan recipes to
    entree_recipes = []
    for meat_type, courses in recipes['savory'].items():
        if 'entree' in courses['course']:
            entree_recipes.extend(courses['course']['entree']['recipes'].keys())

    # Confirm at least 5 recipes exist
    if len(entree_recipes) < 5:
        return "Not enough entree recipes to generate a meal plan."

    # Randomly select recipes from entree options
    meal_plan = random.sample(entree_recipes, 5)
    return meal_plan

# 3. Main Program Loop
def main():
    """
    Main function to run the recipe book application. 
    Provides a command-line interface for interacting with the recipe book functionalities.
    """
    # Load JSON file
    recipes = load_recipes_from_json()

    # Create user-interface list
    while True:
        print("\n1. View Recipes\n2. Add Recipe\n3. Edit Recipe\n4. Delete Recipe\n5. Generate Grocery List / View Recipe Ingredients\n6. Select Random Recipe\n7. Select Random Recipe by Criteria\n8. Generate Meal Plan\n9. Exit\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_recipes(recipes)
        elif choice == '2':
            add_recipe(recipes)
        elif choice == '3':
            edit_recipe(recipes)
        elif choice == '4':
            delete_recipe(recipes)
        elif choice == '5':
            recipe_names = input("Enter recipe names for grocery / ingredient list (comma-separated): ").split(',')
            print("\n", generate_grocery_list(recipes, recipe_names))
        elif choice == '6':
            print("\n", "Selected Recipe:", select_recipe_randomly(recipes))
        elif choice == '7':
            print("\nSelected Recipe:", select_recipe_by_criteria(recipes))
        elif choice == '8':
            print("\nWeekly Meal Plan:", generate_meal_plan(recipes))
        elif choice == '9':
            break
        # Validate user input
        else:
            print("Invalid choice. Please try again.")
        # Save any input recipes
        save_recipes_to_json(recipes)

if __name__ == "__main__":
    main()