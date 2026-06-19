"""
Parking Fee Calculator
---------------------------------------------------
features implemented : done
Different rates for Cars, Bikes, and Trucks
Weekend parking charges
GST calculation
Lost ticket penalty
Night parking discount
---------------------------------------------------
additional features:
Monthly parking passes
VIP parking membership discounts
Receipt number generation
"""

print("We welcome you to Python Parking System. \n")
print("Parking charges are as follows- ")
print("We charge ₹20/hour for hours between 1 - 2.")
print("We charge ₹15/hour for hours between 3 - 5.")
print("We charge ₹10/hour for hours between 6 - 10.")
print("We charge ₹10/hour for hours above 10 with surcharge of ₹150.\n")
print("Bike charges - ₹10.")
print("Car charges - ₹20.")
print("Truck charges - ₹50.")
print("GST = 18% \n")
print("Night Parking Discount: ₹25\n")
print("Lost Ticket Penalty - ₹100\n")

vehicle_number = input("Enter your vehicle number: ")
hours_parked = int(input("Enter number of hours parked: "))
vehicle_type = input("Bike, Car or a Truck?: ").upper()
parking_on_weekends = input("Weekend Parking? (YES/NO): ").upper()
penalty_ticket = input("Do you have a ticket with you? (YES/NO): ").upper()
night_parking = input("Are you going to park your vehicle overnight? (YES/NO): ").upper()

if vehicle_type in ["BIKE", "CAR", "TRUCK"]:
    print("Your receipt generated below:\n")

    if vehicle_type == "BIKE":
        vehicle_charges = 10
    elif vehicle_type == "CAR":
        vehicle_charges = 20
    else:
        vehicle_charges = 50

    if parking_on_weekends == "YES":
        weekend_charges = 100
    elif parking_on_weekends == "NO":
        weekend_charges = 0
    else:
        print("Invalid input. Choose YES or NO.\n")
        weekend_charges = 0

    if penalty_ticket == "YES":
        ticket_available = 0
    elif penalty_ticket == "NO":
        ticket_available = 100
    else:
        print("Invalid input. Choose YES or NO.\n")
        ticket_available = 0

    if night_parking == "YES":
        discount_night_parking = 25
    elif night_parking == "NO":
        discount_night_parking = 0
    else:
        print("Invalid input. Choose YES or NO.\n")
        discount_night_parking = 0

    if len(vehicle_number) == 10 and vehicle_number.isalnum():

        if hours_parked <= 0:
            print("Invalid hours. \n")

        elif 1 <= hours_parked <= 2:
            add_20 = hours_parked * 20
            total_amount = add_20
            receipt_amount = weekend_charges + total_amount + vehicle_charges

            print(f"Parking charges: ₹{add_20}")
            print(f"Vehicle charges: ₹{vehicle_charges}")
            print(f"Weekend parking charges: ₹{weekend_charges}")
            print(f"Penalty amount: ₹{ticket_available}")
            print(f"Discount on night parking: ₹{discount_night_parking}")
            gst_18 = (receipt_amount * 18) / 100
            print(f"GST (18%): ₹{gst_18:.2f}")
            total_receipt_amount = receipt_amount + gst_18 + ticket_available - discount_night_parking
            print(f"Total amount: ₹{total_receipt_amount}\n")

        elif 3 <= hours_parked <= 5:
            add_15 = hours_parked * 15
            total_amount = add_15
            receipt_amount = weekend_charges + total_amount + vehicle_charges

            print(f"Parking charges: ₹{add_15}")
            print(f"Vehicle charges: ₹{vehicle_charges}")
            print(f"Weekend parking charges: ₹{weekend_charges}")
            print(f"Penalty amount: ₹{ticket_available}")
            print(f"Discount on night parking: ₹{discount_night_parking}")
            gst_18 = (receipt_amount * 18) / 100
            print(f"GST (18%): ₹{gst_18:.2f}")
            total_receipt_amount = receipt_amount + gst_18 + ticket_available - discount_night_parking
            print(f"Total amount: ₹{total_receipt_amount}\n")

        elif 6 <= hours_parked <= 10:
            add_10 = hours_parked * 10
            total_amount = add_10
            receipt_amount = weekend_charges + total_amount + vehicle_charges

            print(f"Parking charges: ₹{add_10}")
            print(f"Vehicle charges: ₹{vehicle_charges}")
            print(f"Weekend parking charges: ₹{weekend_charges}")
            print(f"Penalty amount: ₹{ticket_available}")
            print(f"Discount on night parking: ₹{discount_night_parking}")
            gst_18 = (receipt_amount * 18) / 100
            print(f"GST (18%): ₹{gst_18:.2f}")
            total_receipt_amount = receipt_amount + gst_18 + ticket_available - discount_night_parking
            print(f"Total amount: ₹{total_receipt_amount}\n")

        else:
            surcharge_fee = (hours_parked * 10) + 150
            total_amount = surcharge_fee
            receipt_amount = weekend_charges + total_amount + vehicle_charges

            print(f"Parking charges: ₹{surcharge_fee}")
            print(f"Vehicle charges: ₹{vehicle_charges}")
            print(f"Weekend parking charges: ₹{weekend_charges}")
            print(f"Penalty amount: ₹{ticket_available}")
            print(f"Discount on night parking: ₹{discount_night_parking}")
            gst_18 = (receipt_amount * 18) / 100
            print(f"GST (18%): ₹{gst_18:.2f}")
            total_receipt_amount = receipt_amount + gst_18 + ticket_available - discount_night_parking
            print(f"Total amount: ₹{total_receipt_amount}\n")

    else:
        print("The vehicle number is invalid. \n")

else:
    print("Invalid Vehicle type.\n")

print("Thank you again for using Python Parking System. Have a lovely day ahead.")
