"""
Income Tax Calculator
Input annual income.
Apply tax slabs using conditions.
Example:
Up to 3L → 0%
3L–7L → 5%
7L–10L → 10%
Above 10L → 20%
"""

print("Program to print Income Tax Calculator.")
annual_income = float(input("Enter the annual income: "))

if annual_income > 0 and annual_income <= 300000:
  print("There is no tax slab for you.")

elif annual_income > 300000 and annual_income <= 700000:
  tax_5 = annual_income * 0.05
  print(f"You fall under 5% of tax slab and the tax you need to pay is {tax_5}")

elif annual_income > 700000 and annual_income <= 1000000:
  tax_10 = annual_income * 0.10
  print(f"You fall under 10% of tax slab and the tax you need to pay is {tax_10}")

elif annual_income > 1000000:
  tax_20 = annual_income * 0.20
  print(f"You fall under 20% of tax slab and the tax you need to pay is {tax_20}")

else:
  print("Annual Income should be more than zero.")
