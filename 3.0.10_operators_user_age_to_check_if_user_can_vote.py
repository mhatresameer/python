# Level 8: Real Interview Coding Problems

"""
Take age as input.
Print:
Eligible
if age is at least 18.
"""

user_age_for_vote = int(input("You are eligible to vote if your age falls above 18. Enter your age to check if you are eligible to vote or not: "))
# print("\n")

result = user_age_for_vote >= 18
print(f"Are you eligible according to your age to vote? {result}.")
