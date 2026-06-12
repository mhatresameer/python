"""
Smallest of Three Numbers
Input three numbers.
Print the smallest.
"""

print(f"Program to print smallest of three numbers.")

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

if first_num < second_num:
  print(f"{first_num} is smaller.")
elif second_num < third_num:
  print(f"{second_num} is smaller.")
else:
  print(f"{third_num} is smaller.")
