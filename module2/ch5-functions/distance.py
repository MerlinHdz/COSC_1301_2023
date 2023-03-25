# Merlin Hernandez (55096)
# Program Complete
"""
This file contains one function - falling_distance -
which takes as a parameter a number (seconds) and calculates the falling distance
of an object on earth.
"""

GRAVITY = 9.8 # meters per second

# function to get the falling distance of an object given the seconds or time 
def falling_distance(seconds):
    return (GRAVITY * (seconds ** 2)) / 2