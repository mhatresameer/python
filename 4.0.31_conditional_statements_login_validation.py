"""
Login Validation
Input:
Username
Password
Rules:
Username must not be empty.
Password must be at least 8 characters.
Only then print "Login Accepted".
"""

from getpass import getpass

print("Login to access the website.\n")

username = input("Enter your username: ")
password = getpass("Enter the password: ")

if not username:
  print("Username is incorrect. Please retry again.")
elif len(password) <= 8:
  print("Password is incorrect. Please try again.")
else:
  print(f"Welcome {username}. Thank you for logging in.")
