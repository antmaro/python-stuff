#!/usr/bin/env python3

is_raining = input("It is raining? (yes/no): ")

answer = str.lower(is_raining)

if answer == "yes":
    is_windy = input("It is windy? (yes/no): ")
    windy_answer = str.lower(is_windy)
    if windy_answer == "yes":
        print("It is too windy for an umbrella")
    else: 
        print("Take an umbrella")
else:
    print("Enjoy your day")