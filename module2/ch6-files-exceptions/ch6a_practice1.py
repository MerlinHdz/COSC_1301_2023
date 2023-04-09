# Merlin Hernandez (55096)
# Program Complete

'''
This program will open an output file named "my_name.txt"
Then it will prompt the user for two names and one integer value for age.
Lastly, those values will be written to the file.
'''

# Open a file
my_file = open("./my_name.txt", "w")

# Ask for user's name
name = input("Enter your name: ")
name2 = input("Enter someone's name: ")

# Ask for user's age
age = int(input("Enter your age: "))

# Write names to the file
my_file.write(name +  '\n')
my_file.write(name2 + '\n')

# Write age to the file
my_file.write(str(age) + '\n')

# Close the file
my_file.close()