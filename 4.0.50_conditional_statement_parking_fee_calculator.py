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
---------------------------------------------------
additional features:
Different rates for Cars, Bikes, and Trucks
Weekend parking charges
Lost ticket penalty
Night parking discount
Monthly parking passes
GST calculation
VIP parking membership discounts

Multiple vehicles
GST (18%)
VIP parking pass
Lost ticket fine
Overnight parking surcharge
Receipt number generation
"""

print("We welcome you to Python Parking System. \n")

print("Bike charges - ₹10, Car charges - ₹20, Truck charges - ₹50.\n.")
print("Parking charges are as follows- ")
print("We charge ₹20/hour for hours between 0 - 2.")
print("We charge ₹15/hour for hours between 3 - 5.")
print("We charge ₹10/hour for hours between 6 - 10.")
print("We charge ₹10/hour for hours above 10 with surcharge of ₹150.\n")

vehicle_number = input("Enter your vehicle number: ")
hours_parked = int(input("Enter number of hours parked: "))
vehicle_type = input("Bike, Car or a Truck?: ").upper()

if vehicle_type in ["BIKE", "CAR", "TRUCK"]:
    print(f"Your vehicle type is {vehicle_type}.")

    if vehicle_type == "BIKE":
        vehicle_charges = 10

    elif vehicle_type == "CAR":
        vehicle_charges = 20

    else:
        vehicle_charges = 50

    if len(vehicle_number) == 10 and vehicle_number.isalnum():
    
        if hours_parked <= 0:
            print(f"Invalid hours. \n")

        elif 1 <= hours_parked <= 2:
            print("Thank you for entering your details here, please find your receipt: \n")
            add_20 = hours_parked * 20
            print(f"You have parked your {vehicle_type} for {hours_parked} hour(s).")
            print(f"The final amount to be paid is ₹{add_20 + vehicle_charges}.\n")

        elif 3 <= hours_parked <= 5:
            print("Thank you for entering your details here, please find your receipt: \n")
            add_15 = hours_parked * 15
            print(f"You have parked your {vehicle_type} for {hours_parked} hour(s).")
            print(f"The final amount to be paid is ₹{add_15 + vehicle_charges}.\n")


        elif 6 <= hours_parked <= 10:
            print("Thank you for entering your details here, please find your receipt: \n")
            add_10 = hours_parked * 10
            print(f"You have parked your {vehicle_type} for {hours_parked} hour(s).")
            print(f"The final amount to be paid is ₹{add_10 + vehicle_charges}.\n")

        else:
            surcharge_fee = (hours_parked * 10) + 150
            print("Thank you for entering your details here, please find your receipt: \n")
            print(f"You have parked your {vehicle_type} for {hours_parked} hour(s). There is surcharge fee of ₹150 on your total amount.")
            print(f"The amount to be paid is ₹{surcharge_fee}.")
            print(f"The final amount to be paid is ₹{surcharge_fee + vehicle_charges}.\n")

    else:
        print("The vehicle number is invalid. \n")

else:
    print("Invalid Vehicle type.")

print(f"Thank you again for using Python Parking System.")
print(f"Have a lovely day ahead.")
