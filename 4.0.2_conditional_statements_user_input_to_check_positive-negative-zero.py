# Level 1: Basic if / else

"""
2. Positive, Negative, or Zero
Take a number as input and print exactly one of:
Positive
Negative
Zero
"""

check_positive_negative_zero = int(input("Enter number to check if the number is postive, negative or zero: "))

if check_positive_negative_zero > 0:
  print("Positive")
elif check_positive_negative_zero < 0:
  print("Negative")
else:
  print("Zero")
