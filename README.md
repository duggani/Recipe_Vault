# Recipe_Vault

The Recipe Vault Application is a Python-based command-line program designed to manage a digital collection of recipes. This application allows users to view, add, edit, and delete recipes, generate grocery lists, create weekly meal plans, and select recipes based on specific criteria.


## Setup

### Requirements

Python 3.0+

## Installation

1. Ensure Python 3.x is installed on your system.
2. Clone or download the application files from the repository: recipe_book_application.py and recipes.json
3. The application uses a JSON file (recipes.json) to store the recipes. Make sure this file is in the same directory as the script (recipe_book_application.py).

    
## Usage

Go to the project directory

```bash
  cd <project directory>
```

## Start the program

```bash
  python recipe_book_application.py
```
## General Usage Notes
• When using the "Generate Grocery List / View Recipe Ingredients" option, be sure to enter the recipe name exactly as written in the program (case sensitive). To view all recipe names, you can first utilize Option 1 "View Recipes" to see the names for all recipes. If generating a grocery list 
for more than one recipe, enter recipe names exactly as spelled in the program, seperated by a comma, with no spaces before or after the comma. 
Spaces shown in recipe names should be included. 

• To view individual recipe ingredients and ingredient amounts, first utilize Option 1 "View Recipes" to locate desired recipe. 
Then utilize Option 5 "Generate Grocery List / View Recipe Ingredients" to print out ingredients and amounts.

## Features

1. View Recipes
• Displays all recipes categorized by meat type and course type.

2. Add Recipe
• Allows adding a new recipe, including details such as meat type, course type, ingredients,    preparation time, and page number.

3. Edit Recipe
• Enables editing existing recipes in the collection.

4. Delete Recipe
• Permits deletion of recipes from the collection.

5. Generate Grocery List
• Generates a grocery list based on selected recipes.

6. Select Random Recipe
• Generates a grocery list based on selected recipes.

7. Select Recipe by Criteria
• Selects a recipe based on user-selected meat type and course type. Users can choose from a list of available options.

8. Generate Meal Plan
• Creates a weekly meal plan by randomly selecting 5 entree recipes.

## Contributing

Contributions are always welcome! Please ensure to follow best practices for coding and documentation.


## Troubleshooting

Windows users may encounter a KeyError when first attempting to use some functionality within this program. If you encounter this error, confirm that the JSON file has not been altered or corrupted during download. 

## Acknowledgements

Geeks for Geeks. (2023, July 27). Read JSON file using Python. GeeksforGeeks. https://www.geeksforgeeks.org/read-json-file-using-python/

Lofaro, L. (n.d.). Working With JSON Data in Python – Real Python. Realpython.com. https://realpython.com/python-json/

O’Connor, L. (2023, December 12). Personal communication [Personal communication].

Oelsner, K. (n.d.). readme.so. Readme.so. https://readme.so/editor

OpenAI. (2023). ChatGPT. Chat.openai.com; OpenAI. https://chat.openai.com/.

Python Software Foundation. (2023a, December 12). 5. Data Structures. Python Documentation. https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary

Python Software Foundation. (2023b, December 12). 7. Input and Output. Python Documentation. https://docs.python.org/3/tutorial/inputoutput.html?highlight=json

Python Software Foundation. (2023c, December 12). Built-in Types. Python Documentation. https://docs.python.org/3/library/stdtypes.html?highlight=dictionary

Python Software Foundation. (2023d, December 12). Json — JSON encoder and decoder — Python 3.10.4 documentation. Docs.python.org. https://docs.python.org/3/library/json.html?highlight=json#module-json

Rischpater, R. (2015). JavaScript JSON Cookbook. Packt Publishing Ltd. https://pepa.holla.cz/wp-content/uploads/2015/11/JavaScript-JSON-Cookbook.pdf

Stack Overflow. (n.d.). Reading JSON from a file. Stack Overflow. Retrieved December 12, 2023, from https://stackoverflow.com/questions/20199126/reading-json-from-a-file

W
