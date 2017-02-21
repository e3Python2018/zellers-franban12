# Zeller’s algorithm computes the day of the week on which a given date will fall (or fell).
# In this exercise, you will write a program to run Zeller’s algorithm on a specific date.
# The program should use the algorithm outlined below to compute the day of the week on which the
# user’s birthday fell in the year you were born and print the result to the screen.

# Get the user's birthday.

# Ask the user for the month of his birth as a number, store it in a temporary variable

# Set A to the month using the following conversion, with March having the value 1, April the
# value 2, . . ., December the value 10, and January and February being
# counted as months 11 and 12 of the preceding year (in which
# case,subtract 1 from C)

# Ask the user for the day of his birth, store it in variable B

# Ask the user for the year of his birth, store it in variable C
# remember to subtract 1 as necessary

# If C is greater than 99, then set D (the century) equal to C / 100 (hint: use integer division)
# Then set C equal to the year of the century (0-99) (hint: use modulo)

# Implement Zeller's algorithm
# W = (13*A - 1) / 5
# X = C / 4
# Y = D / 4
# Z = W + X + Y + B + C - 2*D
# R = the remainder when Z is divided by 7

# The value of R is the day of the week, where 0 represents Sunday, 1 is Monday, . . ., 6 is Saturday. If
# the computed value of R is a negative number, add 7 to get a non negative number between 0 and 6 (you
# don’t need to do this in the code). Print out R. You can check to be sure your code is working by looking at
# http://www.timeanddate.com/calendar/.
# Run some test cases- try today’s date, your birth date, and whatever else interests you!
