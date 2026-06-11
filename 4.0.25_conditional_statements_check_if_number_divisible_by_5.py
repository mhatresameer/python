"""
Divisible by 5
Input a number.
Print whether it is divisible by 5.
"""

check_number = int(input("Enter any number to check if it is divisible by 5 or not: "))

if check_number % 5 == 0:
  print(f"{check_number} is divisible by 5.")
else:
  print(f"{check_number} is NOT divisible by 5.")
