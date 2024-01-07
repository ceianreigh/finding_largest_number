# Assignment 4
# Ask user to input 3 numbers. Find and print the biggest number using only if-else statements.

# pseudocode

# Ask user to input 3 numbers
number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))
number_3 = int(input("Enter number 3: "))

# Find the biggest number using if-else statements
if number_1 > number_2 and number_1 > number_3:
    highest_number = number_1
if number_2 > number_1 and number_2 > number_3:
    highest_number = number_2
if number_3 > number_1 and number_3 > number_2:
    highest_number = number_3
else:
    highest_number = "All numbers are equal."
# Print the biggest number
