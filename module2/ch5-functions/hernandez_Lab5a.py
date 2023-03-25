# Merlin Hernandez (55096)
# Program Complete
''' 
This program will take as input different numeric values - ratings
Then based on the average of the ratings, it will determine the number of stars for a restaurant
'''

def main():
    num_of_ratings = 5 # amount of ratings to determine our average
    rating_sum = 0 # accumulator for the ratings' values

    # Get num_of_ratings numeric ratings for the restaurant from the user. 
    for i in range(num_of_ratings):
        # Priming read
        rating = float(input(f"Enter critic's rating 0-10 ({i+1} of {num_of_ratings}): "))

        # Input validation
        while rating < 0 or rating > 10:
            print("Invalid")
            rating = float(input(f"Enter critic's rating 0-10 ({i+1} of {num_of_ratings}): "))

        rating_sum += rating

    # Calculate the average rating
    average_rating = round(rating_sum / num_of_ratings, 2)

    # Determine number of stars
    determine_stars(average_rating)



# This function will take a numeric value (average of 5 critics' ratings)
# and determine the number of stars for a restaurant
def determine_stars(average_rating):
    stars = 0
    if average_rating >= 9:
        stars = 5
    elif average_rating >= 8:
        stars = 4
    elif average_rating >= 7:
        stars = 3
    elif average_rating >= 6:
        stars = 2
    elif average_rating >= 5:
        stars = 1
    else:
        stars = 0

    # display number of stars
    print(f"\nFor a rating of {average_rating:.2f}: ")
    print(f"{stars * '* '}")

# Call the main function
main()