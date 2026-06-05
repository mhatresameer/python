# Level 3: Nested Conditions

"""
11. ATM Withdrawal
Inputs:
balance
withdrawal amount
PIN correct? (True/False)
Rules:
PIN must be correct
Withdrawal must be positive
Balance must be sufficient
Print an appropriate message for each failure case.
"""

from getpass import getpass
# library imported

register_pin_number = getpass("Register your pin number for your account with Python Bank: ")
print("Thank you for registering your account with us.\n")

# 1. check balance if any amount is available for withdrawl.
check_balance = float(input("Enter your balance to check if any action can be performed: "))
if check_balance > 10000.0:
  print("Welcome to the Python bank.\n")
  
  # 2. withdrawing amount to be entered here.
  withdrawl_amount = float(input("Enter the amount you wish to withdraw from the Python bank. Maximum amount withdrawn would be upto 5000: "))
  if withdrawl_amount <= 5000 and withdrawl_amount >= 0:
    print(f"The amount to be withdrawn is {withdrawl_amount}.\n")

    # 3. checks and confirms pin
    pin_number = getpass("Enter your pin: ")
    if pin_number == register_pin_number:
      print(f"Pin is correct. Thank you for choosing Python bank. Your current balance is {check_balance - withdrawl_amount}.")
    else:
      print("Pin is incorrect.")
    # 2. withdrawing amount to be entered here.
  else:
    print(f"You cannot withdraw amount at this moment.")
    print("\n")

# 1. check balance if any amount is available for withdrawl.
elif check_balance > 0 and check_balance <= 9999.0:
  print("You do not have sufficient balance to perform this action.")
else:
   print("No Balance.")
