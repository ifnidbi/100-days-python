# Day 3 – BMI Calculator
# Calculates and classifies BMI based on fixed weight and height values.
# Uses conditional statements to categorize results as underweight, normal, or overweight.
# Author: ifnidbi
# Date: 2025-06-09

weight = 73
height = 1.85

bmi = weight / (height ** 2)

# Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print('underweight')
elif bmi >= 25:
    print('overweight')
else:
    print('normal weight')
