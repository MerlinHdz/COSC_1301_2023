# Merlin Hernandez (55096)
# Program Complete

'''
This program asks the user for a date in the format mm/dd/yyy and prints the same date in the format
January 01, 2000 (for example)
'''

def main():
    # Get date from user
    date = input("Enter a date in the format mm/dd/yyy: ")

    # Split the string
    date_info = date.split("/")
    
    # create a list with all the months
    months = ["January", "February", "March", "April", "May", "June", "July", "August",\
              "September", "October", "November", "December"]
    
    # Check which month the user entered
    user_month = date_info[0]

    # store text version of that month in a variable
    month = months[int(user_month)-1]

    # Fill the new_date string
    new_date = f'{month} {date_info[1]}, {date_info[2]}'

    # Print the new date
    print(new_date)


if __name__ == "__main__":
    main()