# Level 1: Basic if / else

"""
3. Voting Eligibility
Take age as input.
Print Eligible if age is at least 18, otherwise Not Eligible.
"""

check_vote_availibility = int(input("Enter age to check if you are eligible to vote or not: "))

if check_vote_availibility >= 18:
  print(f"You are eligible to vote.")
else:
  print(f"You are NOT eligible to vote.")
