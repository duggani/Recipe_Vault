'''
Ian Duggan
CS 5001 Final Project
Fall Semester 2023
Digital Recipe Book Application - TEST SUITE
'''
import unittest
from unittest.mock import patch
from recipe_book_application import load_recipes_from_json, save_recipes_to_json, add_recipe, view_recipes, edit_recipe, delete_recipe, select_recipe_randomly, select_recipe_by_criteria, generate_grocery_list, generate_meal_plan

# Create a class for testing
class TestRecipeBookApplication(unittest.TestCase):

    def setUp(self):
        # Setup a temporary recipes dictionary for testing
        self.test_recipes = {
            'savory': {
                'chicken': {
                    'course': {
                        'entree': {
                            'recipes': {
                                'Test Chicken Recipe': {
                                    'prep time': 30,
                                    'ingredients': ['chicken', 'spices'],
                                    'amount': ['1 kg', 'to taste'],
                                    'page': 10
                                }
                            }
                        }
                    }
                },
                'beef': {
                    'course': {
                        'appetizer': {
                            'recipes': {
                                'Test Beef Recipe': {
                                    'prep time': 20,
                                    'ingredients': ['beef', 'sauce'],
                                    'amount': ['500 g', '2 tbsp'],
                                    'page': 5
                                }
                            }
                        }
                    }
                }
            }
        }

        # Setup a mock file path
        self.mock_file_path = 'test_recipes.json'

        # Patch the filename in the application to use the mock file path
        self.patcher = patch('recipe_book_application.filename', self.mock_file_path)
        self.patcher.start()

    def test_load_recipes_from_json(self):
        # Assuming 'test_recipes.json' is a valid file for testing
        with patch('recipe_book_application.filename', 'test_recipes.json'):
            recipes = load_recipes_from_json()
            self.assertIsInstance(recipes, dict)  # Check if it returns a dictionary

    def test_save_recipes_to_json(self):
        # Create a test dictionary
        test_data = {'test': 'data'}
        # Mocking open to avoid actual file operations
        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            save_recipes_to_json(test_data)
            mock_file.assert_called_once()  # Check if file open was called

    def test_add_recipe(self):
    # Mock user inputs for add_recipe function
    # Ensure there are enough inputs for each prompt in the actual function
        user_inputs = ['1', '1', 'Test Recipe', '20', 'ingredient1,ingredient2', '1,2', '5']
        with patch('builtins.input', side_effect=user_inputs):
            add_recipe(self.test_recipes)
            # Check if the recipe is added under the correct meat and course type
            self.assertIn('Test Recipe', self.test_recipes['savory']['chicken']['course']['entree']['recipes'])

    def test_view_recipes(self):
        # Mock print to capture view_recipes output
        recipes = {'savory': {'chicken': {'course': {'entree': {'recipes': {'Test Recipe': {'prep time': 20, 'page': 5}}}}}}}
        with patch('builtins.print') as mock_print:
            view_recipes(recipes)
            mock_print.assert_called()  # Check if print was called

    def test_edit_recipe(self):
        #tests program ability to edit an existing recipe
        user_inputs = ['1', '1', 'Test Chicken Recipe', '45', 'new_ingredient', 'new_amount', '11']
        with patch('builtins.input', side_effect=user_inputs):
            edit_recipe(self.test_recipes)
            edited_recipe = self.test_recipes['savory']['chicken']['course']['entree']['recipes']['Test Chicken Recipe']
            self.assertEqual(edited_recipe['prep time'], 45)
            self.assertIn('new_ingredient', edited_recipe['ingredients'])


    def test_delete_recipe(self):
        #tests program ability to delete an existing recipe
        user_inputs = ['1', '1', 'Test Chicken Recipe']
        with patch('builtins.input', side_effect=user_inputs):
            delete_recipe(self.test_recipes)
            self.assertNotIn('Test Chicken Recipe', self.test_recipes['savory']['chicken']['course']['entree']['recipes'])


    def test_select_recipe_randomly(self):
        #test program to select a recipe at random
        selected_recipe = select_recipe_randomly(self.test_recipes)
        self.assertIsInstance(selected_recipe, str)


    def test_select_recipe_by_criteria(self):
        #test program to randomly select a recipe after criteria has been input
        user_inputs = ['1', '1']
        with patch('builtins.input', side_effect=user_inputs):
            selected_recipe = select_recipe_by_criteria(self.test_recipes)
            self.assertIsInstance(selected_recipe, str)


    def test_generate_grocery_list(self):
        #test to generate a grocery list based on input recipe
        recipe_names = ['Test Chicken Recipe']
        grocery_list = generate_grocery_list(self.test_recipes, recipe_names)
        self.assertIn('chicken', grocery_list)
        self.assertIn('spices', grocery_list)


    def test_generate_meal_plan(self):
        #test to generate a meal place by randomly selecting 5 recipes
        meal_plan = generate_meal_plan(self.test_recipes)
        self.assertEqual(len(meal_plan), 5)


    def tearDown(self):
        # Stop the patcher after tests are done
        self.patcher.stop()

if __name__ == '__main__':
    unittest.main()
