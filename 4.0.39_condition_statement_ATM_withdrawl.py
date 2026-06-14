"""
ATM Withdrawal
Input:
Balance
Withdrawal amount
Conditions:
Amount must be multiple of 100.
Sufficient balance required.
Then allow withdrawal.
"""

user_balance = int(input("Enter the balance from the account: "))
withdrawl_amount = int(input("Enter the amount to be withdrawn: "))

# check sufficient balance - start
if user_balance > 0:
  print(f"Sufficient balance. You can withdraw amount.")
  # print("\n")
  
  if withdrawl_amount % 100 == 0:
    print(f"Thank you for withdrawing from Python Bank. Your current balance is {user_balance - withdrawl_amount}.")
  else:
    print(f"Only amount with multiples of 100 can be withdrawed at this moment.")

# check sufficient balance - end
else:
  print(f"No sufficient balance found.")
