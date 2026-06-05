

"""
5. Pass or Fail
Take marks (0–100).
Print Pass if marks are at least 40, otherwise Fail.
"""

check_pass_fail = int(input("Enter the marks between 0-100 to check if you are passed or failed: "))

if check_pass_fail >= 40:
  print(f"Student has scored {check_pass_fail} and is passed.")
else:
  print(f"Student has scored {check_pass_fail} and is failed.")
