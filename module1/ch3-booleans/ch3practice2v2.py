# Merlin Hernandez (55096)
# Program Complete
'''
This program will ask the user for a number from 1-7 and display the equivalent day
Monday = 1, Sunday = 7, etc. If a number outside the range 1-7 is given, an error message will be displayed
'''

# Get input from user.
num = int(input("Enter a number from 1-7: "))

if num == 1:
    print("Monday")
else:
    if num == 2:
        print("Tuesday")
    else:
        if num == 3:
            print("Wednesday")
        else:
            if num == 4:
                print("Thursday")
            else:
                if num == 5:
                    print("Friday")
                else:
                    if num == 6:
                        print("Saturday")
                    else:
                        if num == 7:
                            print("Sunday")
                        else:
                            print("Invalid number.")