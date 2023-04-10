# Merlin Hernandez (55096)
# Program Complete
'''
Random Number File Writer - This program writes random numbers to a file, the user will 
be able to specify how many of them they want. The numbers will be in the range of 1-500
'''
import random

# Variables
start, stop = 1, 500 # values for the range from which the numbers will be randomly picked.
file_name = "random_numbers.txt" # name choses for our file, modify this variable if desired.

def main():
    # Print some information for the user
    print("This program will write random numbers from 1-500 to a file")

    # Input validation
    valid_num = False
    while not valid_num:
        try:
            # try converting user input to an int, if this fails a ValueError will be raised
            amount = int(input("Enter amount of numbers: "))

            # if number given by user is less than or equal to zero, raise an error
            if amount <= 0:
                raise ValueError
            
            valid_num = True

        except ValueError:
            print("Invalid input, number must be an integer and greater than zero")


    try:
        # Open or create file - random_numbers.txt
        nums_file = open(file_name, "w")

        # Write numbers to file
        for i in range(amount):
            num = random.randint(start, stop)
            nums_file.write(str(num) + '\n')

        # Display a success message
        print(f"{amount} random numbers were written to this file: {file_name}")

        # Close the file
        nums_file.close()

    except IOError:
        print("Could not open file.")
    except:
        print("An error has ocurred.")


if __name__ == "__main__":
    main()