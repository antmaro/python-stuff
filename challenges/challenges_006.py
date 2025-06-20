#!/usr/bin/env python3

"""Ask how many slices of pizza the user started with
and ask how many slices they have eaten.
Calculate how many slices are left and display the answer in a user-friendly format.
"""

started_slices = int(input("Enter the number of slices you starte with: "))
finish_slices = int(input("How many slices you have eaten: "))
left_slices = started_slices - finish_slices
print("You have", left_slices, "slices remaining.")