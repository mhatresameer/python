# Level 4: Interview Coding Problems
""" Exercise 15: Simple Interest. Store in variables and calculate.
Formula:
SI = (P * R * T) / 100 """

user_input = int(input("Enter the amount here: "))
user_principle = float(input("Enter the priniple to calculate simple interest: "))
user_rate = float(input("Enter the rate to calculate simple interest: "))
user_time = float(input("Enter the time to calculate simple interest: "))

simple_interest = (user_principle * user_rate * user_time) / 100
print(simple_interest)
