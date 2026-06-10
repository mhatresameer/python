"""
Positive, Negative, or Zero

Input a number.
Positive
Negative
Zero
"""

check_number = int(input("Enter a number to check positive, negative or zero: "))

if check_number > 0:
  print("POSITIVE.")
elif check_number < 0:
  print("NEGATIVE.")
else:
  print("ZERO.")
