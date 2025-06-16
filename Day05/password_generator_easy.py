# Day 5 – Easy Password Generator
# Generates a password by concatenating random letters, symbols, and numbers in order.
# Inputs:
#   - Number of letters
#   - Number of symbols
#   - Number of numbers
# Does not shuffle the result (easy to identify structure).
# Author: ifnidbi
# Date: 2025-06-08

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

password = ""

for i in range(nr_letters):
    password += random.choice(letters)

for i in range(nr_symbols):
    password += random.choice(symbols)

for i in range(nr_numbers):
    password += random.choice(numbers)

print(password)
