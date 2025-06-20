#!/usr/bin/env python3

"""
Ask to enter a number betwen 10 and 20(inclusive).
If the number within the rage, display "Thank you",
otherwise display "Incorrect answer".
"""

number = int(input("Enter a number between 10 and 20: "))

if number >= 10 and number <= 20:
    print("Thank you")
else:
    print("Incorrect answer")