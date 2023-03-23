# Merlin Hernandez (55096)
# Program Complete
'''
This program asks the user for a gross monthly income value, and a monthly deductions value
It calculates and displays net monthly income, gross yearly income and net yearly income.
'''

# Ask user for input
gross_monthly_income = float(input("Enter gross monthly income: "))
monthly_deductions = float(input("Enter monthly deductions: "))

# Calculate net monthly income
net_monthly_income = gross_monthly_income - monthly_deductions
print(f"Monthly net income:  ${net_monthly_income:,.2f}") # display value

# Calculate yearly gross pay and yearly net pay
yearly_gross_income = gross_monthly_income * 12
yearly_net_income = net_monthly_income * 12

# Display both values
print(f"Yearly gross income: ${yearly_gross_income:,.2f}")
print(f"Yearly net income:   ${yearly_net_income:,.2f}")


