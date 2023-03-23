# 3. Land Calculation
'''
One acre of land is equivalent to 43,560 square feet. 
Write a program that asks the user to enter the total square feet in a tract of land 
and calculates the number of acres in the tract.
'''

def get_acres(square_feet):
    SQ_FEET_PER_ACRE = 43560
    return square_feet / SQ_FEET_PER_ACRE


# 4. Total Purchase
'''
A customer in a store is purchasing five items. 
Write a program that asks for the price of each item,
then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 7 percent.
'''

def total_purchase():
    total = 0
    while True:
        price_str = input("Enter the price of an item or type 'done' to finish: ")
        if price_str == "done":
            break
        try:
            price = float(price_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        total += price
    
    total_with_tax = total * 1.07
    print(f"Total with tax: $ {total_with_tax:.2f}")


# 5. Distance Traveled
'''
Distance = Speed x Time
Based on a car's speed, write a program that displays the following:
The distance the car will travel in 6, 10 and 15 hours.
'''
def distance_traveled(speed, time):
    distance = speed * time
    print(f"The distance you traveled is {distance}Km in {time} hours")


# 6. Sales Tax
'''
Ask user amount of purchase. The program will compute state and county sales tax.
Assume the state tax is 5 percent and the county tax 2.5%
Display amount of the purchase, state tax, county tax, total sales tax, and the total.
'''
def sales_total(amount):
    STATE_TAX = 0.05
    COUNTY_TAX = 0.025

    # Get state tax
    state_tax_total = amount * STATE_TAX

    # Get county tax
    county_tax_total = amount * COUNTY_TAX

    # Get sale total
    total = amount + state_tax_total + county_tax_total

    # Display different amounts and total
    print(f'''
    Purchase amount: ${amount:.2f}
    State tax: ${state_tax_total:.2f}
    County tax: ${county_tax_total:.2f}
    Total: ${total:.2f}
    ''')



# 9. Celsius to Fahrenheit Converter.
'''
Write a program that converts Celsius temperatures to Fahrenheit temperatures. 
Formula: F = (9/5)C + 32
'''
def celsius_to_fahrenheit(celsius_degrees):
    return (9 * celsius_degrees)/5 + 32


# 11. Male and Female Percentages
'''
Write a program that asks the user for the number of males and the number of females registered in a class.
The program should display the percentage of males and females in the class.
'''
def female_male_percentages(females, males):
    total_people = females + males
    one_percent = total_people/100

    # Get each percentage
    female_percent = females / one_percent
    male_percent = males / one_percent

    return female_percent, male_percent


