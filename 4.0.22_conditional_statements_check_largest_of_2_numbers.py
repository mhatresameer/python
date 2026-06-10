"""
Largest of Two Numbers

Input two numbers.

Print the larger number.
"""

largest_number_one = int(input("Enter the first number: "))
largest_number_two = int(input("Enter the second number: "))

if largest_number_one > largest_number_two:
  print(f"{largest_number_one} is the largest number.")
elif largest_number_two > largest_number_one:
  print(f"{largest_number_two} is the largest number.")
else:
  print("None is larger. Both are equal numbers.")
