# Merlin Hernandez (55096)
# Program Complete

'''
This program stores 3 dictionaries. All three store the same course numbers as keys. The first one stores 
room numbers as values, the second stores the instructors last names as values and the third
stores the meeting times as values.

The program will prompt the user for a course number, and if it is found in the dictionaries, it will print the
information associated with it, otherwise it will print a message.
'''

# Create dictionary with the course numbers as keys
# As values assign it a list containing room number, instructor last name and meeting time
course_rooms = {"CS101": 3004,"CS102": 4501,"CS103": 6755,"NT110": 1244,"CM241": 1411,}
course_instructors = {"CS101": "Haynes","CS102": "Alvarado","CS103": "Rich","NT110": "Burke","CM241": "Lee",}
course_times = {"CS101": "8:00 a.m.","CS102": "9:00 a.m.","CS103": "10:00 a.m.","NT110": "11:00 a.m.","CM241": "1:00 p.m.",}



def main():

    while True:
        course_num = input("Enter course number or press enter to stop: ")

        # Look up course in dictionary
        if course_num in course_rooms:
            print(course_rooms[course_num], course_instructors[course_num], course_times[course_num])
            print()

        # if user presses enter, break the loop
        elif course_num == '':
            break
        else:
            print("Course not found.\n")



if __name__ == "__main__":
    main()