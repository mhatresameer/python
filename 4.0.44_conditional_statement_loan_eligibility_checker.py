"""
Loan Eligibility Checker
Input:
Age
Salary
Credit Score
Rules:
Approve
Reject
Manual Review
based on multiple conditions.
"""

user_age = int(input("Enter the users age: "))
user_salary = float(input("Enter the users salary: "))
user_credit_score = int(input("Enter the credit score: "))

if user_age > 18:
  print(f"You are above {user_age} years of age and eligible for loan.")

  if user_salary <= 49000:
    print(f"Your salary is {user_salary} and we couldn't approve you for a loan.")

  elif user_salary > 50000:
    print(f"Your salary is {user_salary} and we would love to approve you for a loan.")

    if user_credit_score > 0 and user_credit_score <= 499:
      print(f"Since your credit score is below {user_credit_score}, you are not eligible to take more loans.")\

    elif user_credit_score > 500 and user_credit_score <= 999:
      print(f"You are eligible to take another loan once your previous loan is taken care of.")
    
    else:
      print("The credit score should be more than 0")

  else:
    print("salary should be more than 0.")

else:
  print("You are underage.")
