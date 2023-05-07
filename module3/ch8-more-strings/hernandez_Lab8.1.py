# Merlin Hernandez (55096)
# Program Complete

'''
This program reads a file, and counts how many upper case, lower case characters there are.
It also counts the number of digits and the number of spaces and displays all the counts to the user.
'''

def main():
    # open file in read mode
    my_file = open("text.txt", "r")

    # store file contents in a string
    my_str = my_file.read()

    # define count variables
    upper_count = 0
    lower_count = 0
    digit_count = 0
    space_count = 0

    for char in my_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    # close the file
    my_file.close()


    # Print the different counts
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)
    print("Digits:", digit_count)
    print("Spaces:", space_count)


if __name__ == "__main__":
    main()