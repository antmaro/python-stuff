#!/usr/bin/env python3

"""Ask the user for their name and their age.
Add 1 to their age and display the output:
[Name] next birthday you will be [new age].
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
newAge = age + 1
print(name, "next birthday you will be", newAge)