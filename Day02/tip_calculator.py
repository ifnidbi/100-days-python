print("Welcome to my tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill? "))

total_with_tip = bill + (bill * (tip /100))
total_per_person = total_with_tip / people

print(f'Each person should pay: ${total_per_person:.2f}')