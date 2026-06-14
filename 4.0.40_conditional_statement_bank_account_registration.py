"""
Bank Account Registration
Input:
Username
Password
Confirm Password
Rules:
Username cannot be empty.
Password ≥ 8 chars.
Password and Confirm Password must match.
"""

from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter the password: ")
confirm_password = getpass("Re-enter the password to confirm: ")

if not username:
  print("Username cannot be empty.")
elif len(password) < 8:
  print("Password cannot be less than 8 characters.")

  if password != confirm_password:
    print("Passwords do not match.")
  else:
    print("Passwords do match.")

else:
  print(f"Welcome {username}.")
