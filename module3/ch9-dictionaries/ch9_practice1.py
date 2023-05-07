# Merlin Hernandez (55096)
# Program Complete

'''
This program uses a dictionary to keep records of IATA airport codes with their corresponding names.
It allows the user to look up a code, add a code, change it, save the current data to a file and retrieve that data.
'''
from ch9_practice2 import save_data, read_data

# Constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SAVE = 5
RETRIEVE = 6
QUIT = 7

def main():
    # create dictionary
    # I have prepopulated the dictionary with a couple examples
    airports = {
        'ATL': 'Hartsfield-Jackson Atlanta International Airport',
        'LAX': 'Los Angeles International Airport'
    }

    choice = 0

    while choice != QUIT:
        # Get user's choice
        choice = get_choice()
        
        if choice == 1:
            look_up(airports)
        elif choice == 2:
            add(airports)
        elif choice == 3:
            change(airports)
        elif choice == 4:
            delete(airports)
        elif choice == 5:
            save_data(airports)
        elif choice == 6:
            read_data()
        else:
            break



def get_choice():
    # Give instructions to user
    print()
    print("Airport IATA code lookup")
    print("-------------------------")
    print("1 - Look up an airport code")
    print("2 - Add a new airport")
    print("3 - Change an entry")
    print("4 - Delete an entry")
    print("5 - Save data to a file")
    print("6 - Retrieve data")
    print("7 - Quit the program")
    print()


    # Input validation - keep asking for an input until it is an integer in the valid range
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice >= LOOK_UP and choice <= QUIT:
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter an integer between 1-5")

    return choice


def look_up(dictionary):
    # Get airport code from user
    code = input("Enter an airport code: ")

    # Look it up in the dictionary
    print(dictionary.get(code, "Not found"))


def add(dictionary):
    # Get an IATA code and an airport name
    code = input("Enter airport code: ")
    airport = input("Enter the name of the airport: ")

    if code not in dictionary:
        dictionary[code] = airport
        print("Airport added")
    else:
        print("This airport already exists.")


def change(dictionary):
    # Get code that user wants to change
    code = input("Enter the code you wish to modify: ")

    # Check if code is in dictionary
    if code in dictionary:
        new_name = input("Enter updated name for the airport: ")
        dictionary[code] = new_name
        print("Airport updated")
    else:
        print("Airport does not exist")


def delete(dictionary):
    # Get code the user wants to delete
    code = input("Enter the code you wish to delete: ")

    # Check if code is in dictionary
    if code in dictionary:
        del dictionary[code]
        print("Airport deleted")
    else:
        print("Airport does not exits")



if __name__ == "__main__":
    main()