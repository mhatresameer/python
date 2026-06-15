"""
Parking Fee Calculator

Start
│
├─ Enter Vehicle Number
├─ Enter Hours Parked
│
├─ Hours ≤ 2?
│      └─ Yes → Rate = ₹20/hour
│
├─ Else Hours ≤ 5?
│      └─ Yes → Rate = ₹15/hour
│
├─ Else
│      └─ Rate = ₹10/hour
│
├─ Calculate Fee
│
├─ Hours > 10?
│      └─ Yes → Add ₹50 surcharge
│
└─ Display Total Fee
End

"""

print("We welcome you to Python Parking System. \n")
print("Parking charges are as follows- ")
print("We charge ₹20/hour for hours between 0 - 2.")
print("We charge ₹15/hour for hours between 3 - 5.")
print("We charge ₹10/hour for hours between 6 - 10.")
print("We charge ₹10/hour for hours above 10 with surcharge of ₹50.\n")

vehicle_number = input("Enter your vehicle number: ")
hours_parked = int(input("Enter hours for the car parked: "))

if len(vehicle_number) == 10:

  if hours_parked < 0:
    print("Invalid hours. \n")
  
  elif hours_parked >= 0 and hours_parked <= 2:
    print("Thank you for entering your details here, please find your receipt: \n")
    add_20 = hours_parked * 20
    print(f"You have parked your car for {hours_parked} hour(s). Your total amount to be paid is {add_20}. \n")

  elif hours_parked >= 3 and hours_parked <= 5:
    print("Thank you for entering your details here, please find your receipt: \n")
    add_15 = hours_parked * 15
    print(f"You have parked your car for {hours_parked} hour(s). Your total amount to be paid is {add_15}. \n")

  elif hours_parked >= 6 and hours_parked <= 10:
    print("Thank you for entering your details here, please find your receipt: \n")
    add_10 = hours_parked * 10
    print(f"You have parked your car for {hours_parked} hour(s). Your total amount to be paid is {add_10}. \n")

  else:
    surcharge_fee = (hours_parked * 10) + 50
    print("Thank you for entering your details here, please find your receipt: \n")
    print(f"You have parked your car for {hours_parked} hour(s). There is surcharge fee of ₹50 on your total amount.")
    print(f"The amount to be paid is {surcharge_fee}. \n")

else:
  print("The vehicle number is invalid. \n")

print(f"Thank you again for using Python Parking System.")
print(f"Have a lovely day ahead.")
