# Merlin Hernandez (55096)
# Program Complete

# This program will open a file named "number_list.txt" and read every line (which should be numbers)

# Open file
numbers_file = open("./number_list.txt", "r")

# Read and print each line
for line in numbers_file:
    print(line.rstrip())


# Close the file
numbers_file.close()