# Level 8: Real Interview Coding Problems

"""
A year is a leap year if:
Divisible by 4 Not divisible by 100
OR
Divisible by 400

Example: year = 2024
Output: Leap Year
"""

# leap year
check_leap_year = int(input("Enter the year to check if the year is leap year or not: "))
result = (check_leap_year % 400 == 0) or (check_leap_year % 4 == 0 and check_leap_year != 100)
print(f"Year {check_leap_year} is a {result}.")
