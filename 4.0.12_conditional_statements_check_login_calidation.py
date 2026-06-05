# Level 3: Nested Conditions

"""
12. Login Validation
Inputs:
username
password
Rules:
Username must not be empty
Password must be at least 8 characters
Only if both are valid, print Login accepted
"""

from getpass import getpass

username = input("Enter your name: ")
password = getpass("Enter your password: ")

if not username:
  print("Username cannot be empty.")
elif len(password) <= 8:
  print("Password needs to be more than 8 characters.")
else:
  print("Login successful.")
