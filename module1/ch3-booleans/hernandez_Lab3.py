# Merlin Hernandez (55096)
# Program Complete
'''
This program will ask how many packages a user has bought, based on this information
and on specific quantity discounts, the program will display the total of the order.
'''
# Price of our software package
PACKAGE_PRICE = 149.0

package_quantity = int(input("Enter amount of packages: "))

# Determine the discount rate based on quantity
if package_quantity >= 150:
    discount_rate = 0.4
elif package_quantity >= 100:
    discount_rate = 0.3
elif package_quantity >= 50:
    discount_rate = 0.2
elif package_quantity >= 10:
    discount_rate = 0.1
else:
    discount_rate = 0.0

original_price = PACKAGE_PRICE * package_quantity
final_price = package_quantity * (PACKAGE_PRICE - PACKAGE_PRICE * discount_rate) # quantity times discounted price
discount_total = original_price - final_price

# Display discount amount and final price
print(f"Discount Amount: ${discount_total:,.2f}")
print(f"Final Price:     ${final_price:,.2f}")