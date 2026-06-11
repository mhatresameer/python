"""
Voting Eligibility
Input age.
Age ≥ 18 → Eligible
Else → Not Eligible
"""

user_voting = int(input("Enter the check if you are eligible to vote or not: "))

if user_voting >= 18:
  print("Eligible for voting.")
else:
  print("Not eligible for voting.")
