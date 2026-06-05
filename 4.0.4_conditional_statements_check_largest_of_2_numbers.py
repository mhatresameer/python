# Level 1: Basic if / else

"""
4. Largest of Two Numbers
Take two numbers and print the larger one.
Also handle the case where they are equal.
"""

take_first_number = int(input("Enter the first number to check which number is largest: "))
take_second_number = int(input("Enter the second number to check which number is largest: "))

if take_first_number > take_second_number:
  print(f"First number: {take_first_number} is greater than Second number: {take_second_number}")
elif take_first_number == take_second_number:
  print(f"{take_second_number} is equal to {take_first_number}")
else:
  print(f"Second number: {take_second_number} is greater than First number: {take_first_number}")
