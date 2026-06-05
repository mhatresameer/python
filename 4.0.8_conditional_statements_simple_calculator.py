# Level 2: if / elif / else Chains

"""
8. Simple Calculator
Input:
first number
operator (+, -, *, /)
second number
Use if/elif/else to perform the operation.
Handle division by zero gracefully.
"""

first_number = int(input("Enter first number: "))
operator = input("Enter second number: ")
second_number = int(input("Enter second number: "))

if operator == "+":
  print(f"Addition of {first_number} and {second_number} is {first_number+second_number}")
elif operator == "-":
  print(f"Subtraction of {first_number} and {second_number} is {first_number-second_number}")
elif operator == "*":
  print(f"Multiplication of {first_number} and {second_number} is {first_number*second_number}")
elif operator == "/":
  if second_number == 0:
    print("Divisible by 0")
  else:
    print(f"Division of {first_number} and {second_number} is {first_number/second_number}")
else:
  print("Error")
