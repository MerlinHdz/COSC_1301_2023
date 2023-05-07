# Merlin Hernandez (55096)
# Program Complete

import pickle

'''
This python file has two functions: save_data and read_data.
- save_data takes as argument a dictionary and opens an output file named airports.dat in wb mode.
Then it pickles the data from the dictionary and writes it to the file. 

- read_data opens the previously created airports.dat file in rb mode. Then it loads the data into a variable,
and prints it to the screen
'''

def save_data(dictionary):
    # Open output file
    output_file = open("airports.dat", "wb")

    # Write dictionary data to file
    pickle.dump(dictionary, output_file)

    # Close the file
    output_file.close()



def read_data():
    try:
        # Open input file
        input_file = open("airports.dat", "rb")

        # load data
        data = pickle.load(input_file)

        # print data
        print(data)


    except IOError:
        print("No data has been saved yet.")