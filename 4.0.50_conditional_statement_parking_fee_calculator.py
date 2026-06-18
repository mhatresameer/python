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

"""
additional features:
Different rates for Cars, Bikes, and Trucks
Weekend parking charges
Lost ticket penalty
Night parking discount
Monthly parking passes
GST calculation
VIP parking membership discounts
"""



print("We welcome you to Python Parking System. \n")
print("Parking charges are as follows- ")
print("We charge ₹20/hour for hours between 0 - 2.")
print("We charge ₹15/hour for hours between 3 - 5.")
print("We charge ₹10/hour for hours between 6 - 10.")
print("We charge ₹10/hour for hours above 10 with surcharge of ₹50.")
print("Bike - ₹10.")
print("Car - ₹20.")
print("Truck - ₹50.\n")

vehicle_number = input("Enter your vehicle number: ")
hours_parked = int(input("Enter hours for the car parked: "))
vehicle_type = input("Bike, Car or a Truck?: ").upper()

if vehicle_type in ["BIKE, CAR, TRUCK"]:
    print(f"You vehicle type is {vehicle_type}.")

    if len(vehicle_number) == 10:
    
        if hours_parked < 0:
            print(f"Invalid hours. \n")

        elif hours_parked >= 0 and hours_parked <= 2:
            print("Thank you for entering your details here, please find your receipt: \n")
            add_20 = hours_parked * 20
            print(f"You have parked your {vehicle_type} for {hours_parked} hour(s). Your total amount to be paid is {add_20}. \n")

            if vehicle_type == "BIKE":
                bike_charges = add_20 + 10
                print(f"Your final charge is {bike_charges}.")

            elif vehicle_type == "CAR":
                car_charges = add_20 + 20
                print(f"Your final charge is {car_charges}.")

            else:
                truck_charges = add_20 + 50
                print(f"Your final charge is {truck_charges}.")

        elif hours_parked >= 3 and hours_parked <= 5:
            print("Thank you for entering your details here, please find your receipt: \n")
            add_15 = hours_parked * 15
            print(f"You have parked your {vehicle_type} for {hours_parked} hour(s). Your total amount to be paid is {add_15}. \n")

            if vehicle_type == "BIKE":
                bike_charges = add_15 + 10
                print(f"Your final charge is {bike_charges}.")

            elif vehicle_type == "CAR":
                car_charges = add_15 + 20
                print(f"Your final charge is {car_charges}.")

            else:
                truck_charges = add_15 + 50
                print(f"Your final charge is {truck_charges}.")


        elif hours_parked >= 6 and hours_parked <= 10:
            print("Thank you for entering your details here, please find your receipt: \n")
            add_10 = hours_parked * 10
            print(f"You have parked your {vehicle_type} for {hours_parked} hour(s). Your total amount to be paid is {add_10}. \n")

            if vehicle_type == "BIKE":
                bike_charges = add_10 + 10
                print(f"Your final charge is {bike_charges}.")

            elif vehicle_type == "CAR":
                car_charges = add_10 + 20
                print(f"Your final charge is {car_charges}.")

            else:
                truck_charges = add_10 + 50
                print(f"Your final charge is {truck_charges}.")

        elif hours_parked > 10:
            surcharge_fee = (hours_parked * 10) + 50
            print("Thank you for entering your details here, please find your receipt: \n")
            print(f"You have parked your {vehicle_type} for {hours_parked} hour(s). There is surcharge fee of ₹50 on your total amount.")
            print(f"The amount to be paid is {surcharge_fee}. \n")

            if vehicle_type == "BIKE":
                bike_charges = surcharge_fee + 10
                print(f"Your final charge is {bike_charges}.")

            elif vehicle_type == "CAR":
                car_charges = surcharge_fee + 20
                print(f"Your final charge is {car_charges}.")

            else:
                truck_charges = surcharge_fee + 50
                print(f"Your final charge is {truck_charges}.")

        else:
            print("Invalid hours entered.")

    else:
        print("The vehicle number is invalid. \n")

else:
    print("Invalid Vehicle type.")

print(f"Thank you again for using Python Parking System.")
print(f"Have a lovely day ahead.")
print(f"Have a lovely day ahead.")
