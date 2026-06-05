# Level 1: Basic if / else

"""
1. Even or Odd
Take an integer as input.
Print Even if the number is divisible by 2, otherwise print Odd.
"""

check_even_odd = int(input("Enter any number to check if it is even or odd: "))

if check_even_odd % 2 == 0:
  print(f"The entered number {check_even_odd} is even.")
else:
  print(f"The entered number {check_even_odd} is odd.")
