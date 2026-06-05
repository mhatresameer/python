# Level 2: if / elif / else Chains

"""
7. Month Name
Input a number 1–12.
Print the corresponding month name using if/elif/else (not a dictionary yet).
"""

month_name = int(input("Enter any number between 1-12 to check which aligns with the month:"))

if month_name == 1:
  print(f"Month {month_name} is January.")
elif month_name == 2:
  print(f"Month {month_name} is February.")
elif month_name == 3:
  print(f"Month {month_name} is March.")
elif month_name == 4:
  print(f"Month {month_name} is April.")
elif month_name == 5:
  print(f"Month {month_name} is May.")
elif month_name == 6:
  print(f"Month {month_name} is June.")
elif month_name == 7:
  print(f"Month {month_name} is July.")
elif month_name == 8:
  print(f"Month {month_name} is August.")
elif month_name == 9:
  print(f"Month {month_name} is September.")
elif month_name == 10:
  print(f"Month {month_name} is October.")
elif month_name == 11:
  print(f"Month {month_name} is November.")
elif month_name == 12:
  print(f"Month {month_name} is December.")
else:
  print(f"Not a dictionary yet.")
