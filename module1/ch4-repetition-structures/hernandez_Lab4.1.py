# Merlin Hernandez (55096)
# Program Complete
'''
This program will ask the user for a budgeted amount for the month
Then, it will keep asking for an expense amount until the user wishes to finish
Finally, it will display the amount under or over budget.
'''
# Get budget amount from user, round it to 2 decimals
budget_amount = round(float(input("Enter budget for the month: ")), 2)


expense_amount = float(input("Enter expense amount (0 to exit): ")) # priming read to start our loop
total_spent = 0 # accumulator
while expense_amount != 0:
    total_spent += expense_amount
    expense_amount = float(input("Enter expense amount (0 to exit): "))

print(f"Total spent: ${total_spent:.2f}")

if total_spent > budget_amount:
    print(f"You are ${total_spent - budget_amount:.2f} over budget")
else:
    print(f"You have ${budget_amount - total_spent:.2f} remaining!")