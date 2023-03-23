# Merlin Hernandez (55096)
# Program Complete
'''
This program will ask the user for two numbers - a low and a high number
Then for every number in that range, it will display each value times ten. Finally the sum of all those values will be displayed.
'''

# Get user input
low_num = int(input("Enter starting number: "))
high_num = int(input("Enter ending number: "))

# This first loop will display each number in the iteration and its value times 10
for i in range(low_num, high_num + 1):
    print(f"{i}\t{i*10}")


total = 0 # Accumulator
# This second loop will accumulate all the numbers between the starting point and ending point
for i in range(low_num, high_num + 1):
    total += i

# Display the value of the total variable
print("\nTotal\n----------")
print(f"{total}\t{total*10}")