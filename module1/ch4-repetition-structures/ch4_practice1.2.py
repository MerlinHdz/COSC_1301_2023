# Merlin Hernandez (55096)
# Program Complete
'''
This program will ask the user to enter two numbers, and it will display the sum of the two.
the program will ask the user if they wish to perform another sum, if so it will repeat, otherwise it will terminate.
'''

keep_going = "y"

while keep_going:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))

    print(f"{num1 + num2:.2f}")

    again = input("\nAgain? Yes (Enter y)\tNo (Enter any character) ")
    if again != "y":
        keep_going = False