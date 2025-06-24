# Day 2 – Tip Calculator
# Calculates each person's share of a bill including tip.
# Prompts the user for total bill, desired tip percentage, and number of people.
# Outputs the per-person cost, formatted to two decimal places.
# Author: ifnidbi
# Date: 2025-06-09

print("Welcome to my tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill? "))

total_with_tip = bill + (bill * (tip /100))
total_per_person = total_with_tip / people

print(f'Each person should pay: ${total_per_person:.2f}')
