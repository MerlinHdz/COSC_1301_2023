# Merlin Hernandez (55096)
# Program complete
"""
This program will display the corresponding falling distance to the number of seconds
an object falls. From 1-10
"""
import distance

def main():
    print("Time\tFalling Distance")
    print("------------------------")
    for i in range(10):
        # Call function to get falling distance - which is in the distance module
        f_distance_value = distance.falling_distance(i+1)

        # print i + 1 to represent the seconds, print the distance
        print(f"{i+1}\t{f_distance_value:.2f}")
        print()


# Call main function
if __name__ == "__main__":
    main()