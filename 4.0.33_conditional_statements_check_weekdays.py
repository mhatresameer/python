"""
Day of Week
Input number (1-7).
Print:
Monday
Tuesday
to
Sunday
Else:
Invalid day
"""

days_check = int(input("Enter the days of the week to check what number it falls at: "))

if days_check == 1:
  print("It is Sunday.")
elif days_check == 2:
  print("It is Monday.")
elif days_check == 3:
  print("It is Tuesday.")
elif days_check == 4:
  print("It is Wednesday.")
elif days_check == 5:
  print("It is Thursday.")
elif days_check == 6:
  print("It is Friday.")
elif days_check == 7:
  print("It is Saturday.")
else:
  print("Invalid Day.")
