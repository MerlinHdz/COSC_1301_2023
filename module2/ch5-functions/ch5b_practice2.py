# Merlin Hernandez (55096)
# Program Complete
"""
This program will randomly generate a value for the side of a square. 
Then it will calculate its area and perimeter and display the values.
"""
import random
import square

def main():
    square_side = random.randint(1, 100)
    
    # Call function to get square area 
    square_area = square.square_area(square_side)

    # Call function to get square perimeter
    square_perimeter = square.square_perimeter(square_side)

    # print obtained values
    print(f"Square side: {square_side:.2f}")
    print(f"Square area: {square_area:,.2f}")
    print(f"Square perimeter: {square_perimeter:.2f}")

if __name__ == "__main__":
    main()