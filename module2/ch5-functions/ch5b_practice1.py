# Merlin Hernandez (55096)
# Program Complete
"""
This program will generate a random value for the radius of a circle
Then, using this radius it will calculate the area of the circle
Finally both the radius and the area will be displayed to the user
"""   
import random
import math

def main():
    # Print a message to inform about the program
    print("You're about to see a the radius of a random circle and its area")
    input("Press enter to continue ")
    print()

    # Generate a random floating point number between 1 and 100 for our radius
    radius = round(random.uniform(1.0, 100.0), 2) # round it to 2 decimal places
    area = get_circle_area(radius)

    # Display circle radius and circle area
    print(f"Radius of circle: {radius}")
    print(f"Area of circle:   {area:,.2f}")

def get_circle_area(radius):
    # Calculate circle area - pi * r^2
    circle_area = math.pi * (radius ** 2)
    return circle_area

# Call the main function
main()