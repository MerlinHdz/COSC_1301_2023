# Merlin Hernandez (55096)
# Program Complete
'''
This program will ask the user continuously to enter a number, returning a day of the week
based on this number (1 - Monday, 2 - Tuesday...).
Each time it will also ask if the user wishes to stop, ending the program if they do. 
'''

keep_going = True
while keep_going:
    num = int(input("Enter a number from 1-7 (0 to exit): "))

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
    elif num == 0:
        keep_going = False
    else:
        print("Invalid number")



    