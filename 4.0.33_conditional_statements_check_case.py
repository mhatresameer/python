"""
Character Type
Input one character.
Check:
Uppercase
Lowercase
Digit
Special Character
"""

character = input("Enter the character to check the case: ")

if character.isupper():
  print(f"{character} is an uppercase")
elif character.islower():
  print(f"{character} is an lowercase")
elif character.isdigit():
  print(f"{character} is a digit")
else:
  print(f"{character} is a special Character.")
