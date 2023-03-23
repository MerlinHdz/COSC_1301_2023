# Merlin Hernandez
# Program Complete
'''
This program will ask the user for a positive integer no greater than 15
Then it will ask for a character to use to create a square
Then it will display a square made up of the character the user provided, and the number of rows and columns the user entered.
'''

rows = int(input("Enter a number from 1-15: "))

while rows < 1 or rows > 15:
    print("Invalid number.")
    rows = int(input("Enter a number from 1-15: "))

char = input("Enter a character of your choice: ")
print("")

for i in range(rows):
    for j in range(rows):
        print(f"{char}", end="")
    print("")