# Merlin Hernandez (55096)
# Program Complete

# This program reads from a file named students.txt - which contains several records
# Each record contains two fields - student's name and score - these will be displayed together

# Open file
student_records = open("students.txt", "r")

print("Name" + "\t\t" + "Score")
print("-" * 22)


# Read first line of first record
name = student_records.readline().rstrip('\n')

# If something was read, keep processing
while name != '':
    # read score
    score = student_records.readline().rstrip('\n')

    # display name and score
    print(f'{name}\t{float(score):.2f}')

    # Read first line of next record
    name = student_records.readline().rstrip('\n')


# After exiting the loop, close the file
student_records.close()