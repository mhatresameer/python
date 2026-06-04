# Level 8: Real Interview Coding Problems

"""
Problem 2: Divisible by 5
Take a number as input.
Print:
Divisible
if divisible by 5.
"""

check_divisible = int(input("Enter any number to check if it is divisible by 5 or not?! "))
result = check_divisible % 5 == 0

print(f"The output is {result}")
