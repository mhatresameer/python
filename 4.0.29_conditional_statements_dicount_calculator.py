"""
Discount Calculator
Input purchase amount.
Example:
≥ 5000 → 20%
≥ 3000 → 10%
Otherwise → No discount
Calculate final amount.
"""

print(f"Welcome to Python Mart.\n")
purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount >= 5000:
  discount_20 = purchase_amount * 0.20
  final_price_20 = purchase_amount - discount_20
  print(f"The final purchase amount will be {final_price_20}.\n")
elif purchase_amount >= 3000 and purchase_amount < 5000:
  discount_10 = purchase_amount * 0.10
  final_price_10 = purchase_amount - discount_10
  print(f"The final purchase amount will be {final_price_10}.\n")
else:
  print(f"No discount for shopping under 3000/-.\n")

print(f"Thank you for shopping with us. Have a nice day ahead.")
