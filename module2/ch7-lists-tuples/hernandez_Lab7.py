# Merlin Hernandez (55096)
# Program Complete

'''
This program asks the user for 10 numbers to be stores in a list, and for a number to do a search with.
We will check which numbers in the list are greater than the search number, store them in a new list
and display it to the screen, along with the original list. 
'''

def main():
    # Create a list with 10 elements (integers)
    numbers = [0] * 10

    # for every element in the list, ask the user to enter a number, insert value to list
    for i in range(len(numbers)):
        num = int(input("Enter a number: "))
        numbers[i] = num

    # Ask the user for a number with which we'll narrow down the list of numbers
    search_number = int(input("Number to test if the list elements are greater than: "))

    # perform search
    new_list = display_larger(numbers, search_number)

    # print list of numbers greater than search number
    print(f"List of numbers greater than {search_number}:")
    print(new_list)


def display_larger(list, num):
    narrowed_list = []

    for element in list:
        if element > num:
            narrowed_list.append(element)

    return narrowed_list


if __name__ == "__main__":
    main()