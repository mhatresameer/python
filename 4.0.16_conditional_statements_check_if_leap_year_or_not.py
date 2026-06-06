# Level 4: Classic Interview Problems

"""
16. Leap Year Checker
A year is a leap year if:
divisible by 400
or divisible by 4 but not by 100
Examples:
Year:Result
2024:Leap Year
1900:Not a Leap Year
2000:Leap Year
"""

year = int(input("Enter a year to check if it is a leap year or not: "))

if year % 4 == 0 or year % 400 == 0:
  print("Leap year")
else:
  print("Not a leap year.")
