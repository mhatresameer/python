"""
Largest of Three Numbers
Input three numbers.
Print the largest.
"""

print("Program to print the largest of Three Numbers")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number > second_number:
  print(f"{first_number} is greater.")
elif second_number > third_number:
  print(f"{second_number} is greater")
elif third_number > first_number:
  print(f"{third_number} is greater")
else:
  print(f"Nothing is greater.")
