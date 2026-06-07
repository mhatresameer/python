# Level 4: Classic Interview Problems

"""
18. Number of Digits
Input an integer and print whether it has:
1 digit
2 digits
3 digits
4+ digits
Do this using conditionals (no loops or strings yet).
"""

user_number = int(input("Enter any number to check if it is 1, 2, 3 or 4 digit: "))
print("\n")

if user_number >= 0:
  print(f"{user_number} is positive.")

  if user_number >= 0 and user_number <= 9:
    print(f"{user_number} is a 1 digit number.")
  elif user_number >= 10 and user_number <= 99:
    print(f"{user_number} is a 2 digit number.")
  elif user_number >= 99 and user_number <= 999:
    print(f"{user_number} is a 3 digit number.")
  elif user_number >= 1000 and user_number <= 9999:
    print(f"{user_number} is a 4 digit number.")
  else:
    print(f"{user_number} is beyond 5 digit number.")

else:
  print(f"{user_number} is negative.")
