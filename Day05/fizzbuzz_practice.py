# Day 5 – FizzBuzz Challenge
# Prints numbers from 1 to 100 with special rules:
# - Multiples of 3 print 'Fizz'
# - Multiples of 5 print 'Buzz'
# - Multiples of both 3 and 5 print 'FizzBuzz'
# A classic loop + modulo condition exercise.
# Author: ifnidbi
# Date: 2025-06-08

for i in range(1, 101):
    if (i % 3) == 0 and (i % 5) == 0:
        print('FizzBuzz')
    elif (i % 3) == 0:
        print('Fizz')
    elif (i % 5) == 0:
        print('Buzz')
    else:
        print(i)
