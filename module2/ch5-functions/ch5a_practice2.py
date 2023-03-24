# Merlin Hernandez (55096)
# Program Complete
"""
This program will convert a distance in kilometers to miles. It will get a value in kilometers from 
the user, and call a function to do the conversion and display the value
"""
# Global constant for km/mile conversion factor
KM_TO_MI_FACTOR = 0.6214

def main():
    km_value = float(input("Enter a value in kilometers: "))
    km_to_miles(km_value)

# this function takes a value in kilometers, converts it to miles and prints the new value.
def km_to_miles(kilometers):
    # Using an f string, format the value to have two decimal places.
    print(f"{(kilometers * KM_TO_MI_FACTOR):.2f} Miles")


# Call main function to start the program
main()