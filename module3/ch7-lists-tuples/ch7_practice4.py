# Merlin Hernandez (55096)
# Program Complete
'''
This program creates a 2 dimensional list with 4 rows and 3 columns. For every element in the 2D list,
it asks the user for a number. It then shows the list to the user and displays a total sum of all the elements.
'''

ROWS, COLS = 4, 3

# Create a 2D list
my_2d_list = [[0 for i in range(COLS)] for i in range(ROWS)]


# For every element (COLS total elements) of every list (ROWS total lists) in the 2D list, prompt the user for a value
for row in range(ROWS):
    for col in range(COLS):
        num = int(input(f"Enter value for row {row}, column {col}: "))
        my_2d_list[row][col] = num


# Calculate the sum of all the elements
total = 0
for row in my_2d_list:
    for element in row:
        total += element


# Display the list and the total
print("2D List: ")
for row in my_2d_list:
    print(row)

print(f"Total sum of all elements: {total}")