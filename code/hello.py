#!/bin/env/python
# This program says hello and asks for my name

print('Hello worldl')
print('What is your name?') # aks for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The lenght of your name is: '+ str(len(myName)))
print ('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) +1) + 'in a year')
