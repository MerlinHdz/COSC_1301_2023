# Merlin Hernandez (55096)
# Program Complete
'''
This program will take as input the number of servings of spaghetti sauce the user would like to make.
Based on that number and on a recipe, it will output the amount of every ingredient needed to make those servings.
'''

# Amount of servings needed for 4 servings
RECIPE_TOMATO_SAUCE = 2 # amount in cups
RECIPE_TOMATO_PASTE = 0.33 # amount in cups
RECIPE_GARLIC_CLOVES = 2
RECIPE_OREGANO_TABLESPOONS = 1

# Get input from user
servings = float(input("How many servings of spaghetti sauce do you want to make? "))

# Calculate amounts for servings
servings_tomato_sauce = (RECIPE_TOMATO_SAUCE * servings)/4
servings_tomato_paste = (RECIPE_TOMATO_PASTE * servings)/4
servings_garlic_cloves = (RECIPE_GARLIC_CLOVES * servings)/4
servings_oregano_tablespoons = (RECIPE_OREGANO_TABLESPOONS * servings)/4

# Print how much of each ingredient the user will need
print(
f'''
To make {servings} servings of spaghetti sauce, you will need:\n
{servings_tomato_sauce:.2f} cups of tomato sauce
{servings_tomato_paste:.2f} cups of tomato paste
{servings_garlic_cloves:.2f} garlic cloves
{servings_oregano_tablespoons:.2f} tablespoons of oregano
'''
)