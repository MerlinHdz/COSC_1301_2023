# Merlin Hernandez (55096)
# Program Complete
'''
Lottery number generator - This program generates a 7 digit lottery ticket number and displays it to user.
'''

import random

NUM_LENGTH = 7

def main():
    # Create a list 
    ticket_numbers = [0] * NUM_LENGTH

    for num in range(NUM_LENGTH):
        ticket_numbers[num] = random.randint(0,9)

    # display ticket number - each number in the list
    print("Lottery Ticket")
    for element in ticket_numbers:
        print(element, end="")
    print()

if __name__ == "__main__":
    main()