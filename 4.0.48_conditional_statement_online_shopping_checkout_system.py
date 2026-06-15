"""
Online Shopping Checkout System

Start
│
├─ Enter purchase amount
├─ Enter customer type
│
├─ Is customer VIP?
│      └─ Yes → 20% discount
│
├─ Else is customer Premium?
│      └─ Yes → 10% discount
│
├─ Else is customer Regular?
│      ├─ Amount ≥ 5000?
│      │      └─ Yes → 5% discount
│      └─ No → No discount
│
└─ Display final bill
End

"""

print("Program to print the Online Shopping Checkout System.")
print("Choose from VIP / Premium / Regular while entering Customer Type. \n")

purchase_amount = float(input("Enter the purchase amount: "))
customer_type = input("Enter the type of shopping made. Whether it is VIP or Premium or Regular: ")
print("Thank you for shopping with us. \n")

if customer_type == "VIP":
  print("You are eligible for 20% discount with VIP selection.")
  discount_20 = purchase_amount * 0.20
  final_bill = purchase_amount - discount_20
  print(f"The discount applicable is {discount_20:.2f}. Happy Shopping. \n")

elif customer_type == "Premium":
  print("You are eligible for 10% discount with Premium selection.")
  discount_10 = purchase_amount * 0.10
  final_bill = purchase_amount - discount_10
  print(f"The discount applicable is {discount_10:.2f}. Keep visiting us. \n")

else:

  if purchase_amount >= 5000:
    print("You are eligible for 5% discount with Regular selection.")
    discount_5 = purchase_amount * 0.05
    final_bill = purchase_amount - discount_5
    print(f"The discount applicable is {discount_5:.2f}. More new products will be available soon. \n")

  else:
    print("Python Mart allows no discount for shopping under 5000 on Regular card. \n")

print(f"Your final bill is {final_bill}. Have a nice day ahead.")
