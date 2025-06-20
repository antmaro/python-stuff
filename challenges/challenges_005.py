#!/usr/bin/env python3

"""Ask the user to enter three numbers and Add them
togheter (the first two) and then multiply the result by the third number.
Display the answer as "The total is [answer]"
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
answer = (num1 + num2) * num3
print("The total is: ", answer)