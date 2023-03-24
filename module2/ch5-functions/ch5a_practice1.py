# Merlin Hernandez (55096)
# Program Complete
'''
This program will display the steps for making a sandwich
'''

def main():
    # Display a starting message
    starting_message()

    input("Press Enter to see the first step ")
    # step1
    step1()

    input("Press Enter to see the next step ")
    # step 2
    step2()

    input("Press Enter to see the next step ")
    # step 3
    step3()

    input("Press Enter to see the next step ")
    # step 4
    step4()

    input("Press Enter to see the final step ")
    # step 5
    step5()


# Function to display a message at the beginning of the program
def starting_message():
    print("This program tells you how to prepare a peanut butter and jelly sandwich")
    print("There are five easy steps.")
    print()

def step1():
    print("Step 1: Gather your ingredients and supplies")
    print("Bread, peanut butter, jelly, a butter knife, a plate")
    print()

def step2():
    print("Step 2: Grab two slices of bread and place them on a plate")
    print()

def step3():
    print("Step 3: Using the butter knife, spread peanut butter on a slice of bread")
    print()

def step4():
    print("Step 4: Using your knife, now spread jelly on the other slice of bread")
    print()

def step5():
    print("Step 5: Assemble the sandwich by placing the peanut butter and jelly sides together.")
    print()


# Call the main function to start the program
main()