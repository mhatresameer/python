"""
Month Days
Input month number.
Print:
31 days
30 days
28/29 days
Invalid month
"""
print(f"January:1, February:2, March:3, April:4, May:5, June:6, July:7, August:8, September:9, October:10, November:11, December:12")
month_number = int(input("Enter the number of the month to check how many days are present: "))

if month_number in [1, 3, 5, 7, 10, 12]:
  print(f"{month_number} has 31 days.")
elif month_number in [4, 6, 9, 11]:
  print(f"{month_number} has 30 days.")
elif month_number in [2]:
  print(f"{month_number} has 29 days.")
else:
  print("Invalid Month.")
