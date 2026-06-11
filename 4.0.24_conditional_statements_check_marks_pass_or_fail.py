"""
Pass or Fail
Input marks.
Marks ≥ 35 → Pass
Else → Fail
"""

check_result = int(input("Enter your marks to check if you are passed or failed: "))

if check_result >= 35:
  print("Congratulations. You are passed.")
else:
  print("We regret to inform you that you have NOT passed.")
