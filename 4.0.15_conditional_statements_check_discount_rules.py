# Level 3: Nested Conditions

"""
15. Discount Rules
Inputs:
cart total
premium member? (True/False)
Rules:
Premium + total ≥ 5000 → 20% discount
Premium + total < 5000 → 10% discount
Non-premium + total ≥ 5000 → 5% discount
Otherwise → no discount
Print the discount percentage.
"""

# input amount for total purchased
carts_total = float(input("Enter the total shopping amount: "))
print("\n")
print("Premium Member.")
print("Not a Premium Member.\n")
are_you_a_premium_member = input(f"Are you a premium member? Select Y for Yes and N for No: ")

# are you a discount member - start
if are_you_a_premium_member == "Y":
  print(f"You are a premium member. You are availed for a discount offer.")

  # discounted amounts - start
  if carts_total >= 5000:
    discount_20_percent = carts_total * (0.20/100)
    final_after_20_discount = carts_total - discount_20_percent
    print(f"You are availed for a 20% discount. Your current total bill is {final_after_20_discount}. Happy Shopping.")
  else:
    discount_10_percent = carts_total * (0.10/100)
    final_after_10_discount = carts_total - discount_10_percent
    print(f"You are availed for a 10% discount. Your current total bill is {final_after_10_discount}. Happy Shopping.")
  # discounted amounts - end

elif carts_total >= 5000:
  discount_05_percent = carts_total * (0.05/100)
  final_after_5_discount = carts_total - discount_05_percent
  print(f"You are availed for a 5% discount. Your current total bill is {final_after_5_discount}. Happy Shopping.")
else:
  print(f"No discount availed.")
# are you a discount member - end

# discount_amount = original_price * (discount_percent / 100)
# final_price = original_price - discount_amount
