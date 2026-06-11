"""
Leap Year Check
Input a year.
If divisible by 4 → Leap Year
Else → Not Leap Year
"""

check_leap_year = int(input("Enter the year to check if it is a LEAP year or NOT: "))

if check_leap_year % 4 == 0 or check_leap_year % 400 == 0:
  print(f"{check_leap_year} is a LEAP year.")
else:
  print(f"{check_leap_year} is NOT")
