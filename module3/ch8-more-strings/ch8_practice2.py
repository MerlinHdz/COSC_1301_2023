# Merlin Hernandez (55096)
# Program Complete

'''
This program asks the user to write a sentence. Then it will flip the uppercase letters to lowercase and vice versa
'''

def main():
    print("Write something")
    user_string = input("Include lowercase, uppercase and special characters: ")
    new_string = ""

    for char in user_string:
        if char.islower():
            new_string += char.upper()
        elif char.isupper():
            new_string += char.lower()
        else:
            new_string += char


    print("Original sentence:", user_string)
    print("New sentence:", new_string)

if __name__ == "__main__":
    main()