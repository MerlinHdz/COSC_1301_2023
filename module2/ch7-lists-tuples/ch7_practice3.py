# Merlin Hernandez (55096)
# Program Complete

'''
This program will create two lists of integers. Then it will join those two lists, sort the resulting list,
and add up all its elements. Then it will display the joined list, the total, the maximum and minimum value.
'''

def main():
    list1 = [20, 34, 23, 56, 44]
    list2 = [10, 9, 8, 7, 6]

    combined_list = list1 + list2

    sorted_list = sorted(combined_list)

    # Call the total_list function, store total value in a variable "total"
    total = total_list(sorted_list)

    print(f"Combined list: {sorted_list}")
    print(f"Total: {total}")
    print(f"Maximum value: {max(sorted_list)}")
    print(f"Minimum value: {min(sorted_list)}")



# This function takes a list as an argument (a list of integers) and adds all its elements together
# And returns that value
def total_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == '__main__':
    main()
