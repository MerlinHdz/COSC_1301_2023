# Merlin Hernandez (55096)
# Program Complete

'''
This program opens a file named "my_name.txt" in reading mode
We expect there to be three lines. Line one will have a name, and so will line two. 
Line three should have an integer value. Then the program will print to the screen each of the values,
and also the value of age divided by two
'''

# Open the file
my_file = open("my_name.txt", "r")

# Read first two lines, strip the empty space
name = my_file.readline().rstrip()
name2 = my_file.readline().rstrip()

# Read third line, strip empty space and convert to int
age = int(my_file.readline().rstrip())

# Print values
print(name)
print(name2)
print(f'Age: {age}')
print(f'Half age: {age/2}')

# Close the file
my_file.close()