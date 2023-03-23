# Merlin Hernandez (55096)
# Program Complete
'''
This program will ask the user for a number from 1-7 and display the equivalent day
Monday = 1, Sunday = 7, etc. If a number outside the range 1-7 is given, an error message will be displayed
'''

# Get input from user.
num = int(input("Enter a number from 1-7: "))

# Check if number is within valid range first
if num >= 1 and num <= 7:
    if num == 1:
        print("Monday")
    elif num == 2:
        print("Tuesday")
    elif num == 3:
        print("Wednesday")
    elif num == 4:
        print("Thursday")
    elif num == 5:
        print("Friday")
    elif num == 6:
        print("Saturday")
    elif num == 7:
        print("Sunday")
else:
    print("Invalid number")