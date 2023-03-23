# Merlin Hernandez (55096)
# Program Complete
''' 
This program prompts the user for the price of three items,
then displays the total and average price for the items. 
'''

# Get input from the user
hamburger_price = float(input("How much does the hamburger cost? "))
fries_price = float(input("How much do the fries cost? "))
shake_price = float(input("How much does the shake cost? "))

# Add the integers provided by user
total_price = hamburger_price + fries_price + shake_price

# Calculate average
average_item_price = total_price / 3

print(f"The total price is: ${total_price:.2f}")
print(f"The average price is: ${average_item_price:.2f}")