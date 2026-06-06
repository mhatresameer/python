# Level 3: Nested Conditions

"""
13. Scholarship Eligibility
Inputs:
marks
family income
Eligible if:
marks ≥ 85
income ≤ 300000
Print Scholarship Eligible or Not Eligible.
"""

user_marks = int(input("Enter your marks to check if you are eligible to have scholarship or not?!: "))
user_family_income = float(input("Enter your family income as well: "))

if user_marks >= 85:
  if user_family_income <= 300000:
    print(f"You are eligible for scholarship. Welcome!")
  else:
    print(f"Your family income is beyond limit.")
else:
  print(f"Since your marks are low, you are not eligible for scholarship")
