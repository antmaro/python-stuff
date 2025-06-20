#!/usr/bin/env python3

"""Ask the total price of the bill, then ask how many diners there are.
Divide the total bill by the number of diners and display the amount.
"""

total_price = int(input("Enter the total price of the bill: "))
num_diners = int(input("Enter the number of diners: "))
amount_per_person = total_price / num_diners
print("The price per person is: ", amount_per_person)