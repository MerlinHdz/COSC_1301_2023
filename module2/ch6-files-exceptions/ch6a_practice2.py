# Merlin Hernandez (55096)
# Program Complete

# This program will open an output file, then write the numbers from 50-100 to it using a loop

# Open output file 
my_file = open("./number_list.txt", "w")

# Write to file numbers from 50-100
for i in range(50, 101):
    my_file.write(str(i) + '\n')

# Close the file
my_file.close()