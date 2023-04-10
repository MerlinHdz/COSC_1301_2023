# Merlin Hernandez (55096)
# Program Complete

# This program will read from a list of numbers, calculate the sum and average of all numbers
# and it will display both values. It will also handle possible errors


try:
    # Open file
    numbers_file = open("number_list.txt", "r")

    total_sum = 0
    lines_total = 0

    for line in numbers_file:
        lines_total += 1
        total_sum += int(line)

    # Calculate the average
    average = total_sum / lines_total

    # Display total sum and average
    print(f"Total sum: {total_sum}")
    print(f"Average: {average}")

    # close file
    numbers_file.close()
except IOError:
    print("Cannot open file")

except ValueError:
    print("Non-numeric data found in file.")

except:
    print("An error has ocurred.")