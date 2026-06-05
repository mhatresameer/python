# Level 2: if / elif / else Chains

"""
Given marks:
Range:Grade
90–100:A
75–89:B
60–74:C
40–59:D
Below 40:F
Print the appropriate grade.
Bonus: print Invalid marks if input is outside 0–100.
"""

check_marks = int(input("Enter the number between 0 to 100 to check the grade: "))

if check_marks >= 90 and check_marks <= 100:
  print(f"You have scored {check_marks} and scored 'A' grade.")
elif check_marks >= 75 and check_marks <= 89:
  print(f"You have scored {check_marks} and scored 'B' grade.")
elif check_marks >= 60 and check_marks <= 74:
  print(f"You have scored {check_marks} and scored 'C' grade.")
elif check_marks >= 40 and check_marks <= 59:
  print(f"You have scored {check_marks} and scored 'D' grade.")
elif check_marks < 40:
  print(f"You have scored {check_marks} and scored 'F' grade.")
else:
  print(f"INVALID MARKS.")
