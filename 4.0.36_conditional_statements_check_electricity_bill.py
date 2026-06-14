"""
Electricity Bill
Input units consumed.
Example:
First 100 units → ₹5/unit
Next 100 → ₹7/unit
Above 200 → ₹10/unit
Calculate bill.
"""

print("Program to check electricity bill.")
units_consumed = float(input("Enter the amount of units consumed: "))

if units_consumed > 1 and units_consumed <= 100:
  units_consumed_plus_five = units_consumed + 5
  print(f"You have consumed {units_consumed} units. Your new bill as per ₹5/unit is {units_consumed_plus_five}.")
elif units_consumed > 100 and units_consumed < 200:
  units_consumed_plus_seven = units_consumed + 7
  print(f"You have consumed {units_consumed} units. Your new bill as per ₹7/unit is {units_consumed_plus_seven}.")
elif units_consumed > 200:
  units_consumed_plus_ten = units_consumed + 10
  print(f"You have consumed {units_consumed} units. Your new bill as per ₹10/unit is {units_consumed_plus_ten}.")
else:
  print("The bill should reflect more than ZERO (0) units. Thank you for checking.")
