"""
Employee Bonus
Input:
Salary
Years of service
Rules:
Salary > 50000
Service > 5 years → 15% bonus
Otherwise → 10%
Salary ≤ 50000
Service > 5 years → 8%
Otherwise → 5%
"""

print("Program to check employee bonus.\n")

# inputs - start
employee_salary = float(input("Enter the salary received: "))
employee_years_of_service = float(input("Enter the years of service: "))
print("PLEASE NOTE: The bonus on salary is totally dependant on the percentage provided to your performances. \n")
# inputs - end

if employee_salary > 50000:
  print("You are eligible for bonus this year.")
  if employee_years_of_service > 5:
    bonus_15 = employee_salary * 0.15
    print(f"With an increment of 15% in your salary, we are pleased to offer you {bonus_15} this year.")
  else:
    bonus_10 = employee_salary * 0.10
    print(f"We have incremented 10% of bonus which is {bonus_10} this year and we couldn't be happier.")
else:
  print("You are eligible for bonus this year.")
  if employee_years_of_service > 5:
    bonus_8 = employee_salary * 0.08
    print(f"The new increment of 8% of bonus that makes {bonus_8} has been reflected this year for you. We are more happier.")
  else:
    bonus_5 = employee_salary * 0.05
    print(f"You have received a bonus of 5% this year. The new bonus is {bonus_5}. We wish you all the very best.")
