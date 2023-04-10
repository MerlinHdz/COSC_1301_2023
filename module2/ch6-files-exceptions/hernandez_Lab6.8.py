# Merlin Hernandez (55096)
# Program Complete

'''
Random Number File Reader - This program reads numbers from a file, it displays the numbers,
the sum of all the numbers, the average, and the amount of numbers read from the file.
'''
file_name = "random_numbers.txt"

def main():
    try:
        # Open the file
        nums_file = open(file_name, "r")

        nums_sum = 0 # accumulator for our sum 
        total_lines = 0 # accumulator for number of numbers (quantity)

        for line in nums_file:
            # display line from file, strip empty space
            print(line.rstrip('\n'))

            # Try to convert to integer and add it to accumulator
            nums_sum += int(line)

            # increase line count
            total_lines += 1

        
        print() # empty line
        # display total sum and numbers read
        print(f"Total sum: {nums_sum}")
        print(f"Numbers read: {total_lines}")

        # calculate and display average
        average = nums_sum / total_lines
        print(average)

        # close the file
        nums_file.close()

    except IOError:
        print(f"Could not open file: {file_name}")
    except ValueError:
        print("Non-numeric data found in file.")
    except:
        print("An error has ocurred")


if __name__ == "__main__":
    main()