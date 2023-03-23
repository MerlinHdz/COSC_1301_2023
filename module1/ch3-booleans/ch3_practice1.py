# Merlin Hernandez (55096)
# Program Complete
'''
A date is a magic date is when the month multiplied by the day equals the year in the format (01/23/23)
This program will take as input a month, a day and a year numeric value, and determine if it is a magic date.
'''

# Get user input 
month = int(input("Enter the month : "))
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))

# Check if the month value times the day value equals the year.
if month * day == year:
    print(f"{month}/{day}/{year} is a magic date!")
else:
    print("That is not a magic date.")