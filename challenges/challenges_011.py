#!/usr/bin/env python3

"""Ask for a number over 100 and then enter a number
under 10 and tell them how many times the smaller number goes into the larger number.
"""

larger = int(input("Enter a number over 100: "))
smaller = int(input("Enter a number under 10: "))
answer = larger // smaller

print(smaller, "goes into", larger, answer, "times")

