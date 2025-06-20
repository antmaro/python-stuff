#!/usr/bin/env python3

"""
Enter a number that is under 20.
If the number is 20 or more, display the message "Too high",
otherwise display "Thank you".
"""

number = int(input("Enter a number under 20: "))

if number >= 20:
    print("Too high")
else:
    print("Thank you")