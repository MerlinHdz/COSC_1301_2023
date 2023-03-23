# Merlin Hernandez (55096)
# Program Complete
'''
This program will calculate how much the ocean has risen in a given amount of years
It will use the number 1.8 millimeters per year to perform the calculation
'''

YEARS = 25
RISE_PER_YEAR = 1.8 # millimeters

print("Year\tRise (in millimeters)")
print("-"*30)

# For every year in our range, print the year and the millimeters the ocean has risen
for year in range(YEARS + 1):
    print(f"{year}\t{(year * RISE_PER_YEAR):.2f}")