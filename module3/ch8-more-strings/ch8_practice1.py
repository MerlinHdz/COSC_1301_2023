# Merlin Hernandez (55096)
# Program Complete

'''
This program will accept three strings as input from the user. A first, last and middle name.
Then it will concatenate them together into a single string
It will count how many "a" or "A", how many "e" or "E" and how many "s" "S" there are in the string
And it will display the three counts.
'''

def main():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    middle = input("Enter your middle name: ")

    full_name = first + last + middle

    # define the different count variables
    a_count = 0
    e_count = 0
    s_count = 0

    for char in full_name.lower():
        if char == "a":
            a_count += 1
        elif char == "e":
            e_count += 1
        elif char == "s":
            s_count += 1

    # display the three counts
    print("In your full name, there are:")
    print(f"{a_count} a's")
    print(f"{e_count} e's")
    print(f"{s_count} s's")



# call main
if __name__ == "__main__":
    main()