#!/usr/bin/env python3

fav_colour = input("Enter your favourite colour: ")

answer = str.lower(fav_colour)

if answer == "red":
    print("I like red too.")
else:
    print("I don't like", answer, "I prefer red")