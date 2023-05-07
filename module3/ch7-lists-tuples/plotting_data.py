# Starting Out With Python Chapter 7 - Section 7.11 Plotting list data with the matplotlib package

# matplotlib is not part of the standard Python library, needs to be installed >> sudo pip3 install matplotlib

import matplotlib.pyplot as plt

def main():
     x_coords = [0, 1, 2, 3, 4]
     y_coords = [0, 3, 1, 5, 2]

     # Build the graph
     plt.plot(x_coords, y_coords)

     # Add a title
     plt.title("Sample Data")

     # Add labels to the axes
     plt.xlabel("This is the X axes")
     plt.ylabel("This is the Y axes")

     # Set the axes limit
     plt.xlim(xmin = -1, xmax = 10)
     plt.ylim(ymin = -1, ymax = 6)

     # Add a grid
     plt.grid(True)

     # Display the line graph
     plt.show()


# Call main
if __name__ == "__main__":
    main()

