"""
Passenger Name
Passenger Age
Bus Type (AC / Non-AC / Sleeper)
Number of Tickets
Travel Distance (km)
Travel Day (Weekday / Weekend)

FEATURES THAT CAN BE IMPLEMENTED:
Basic Features
Passenger name validation
  - Age validation
  - Bus type selection
  - Ticket quantity
  - Fare calculation
  - Reservation summary

Intermediate Features
  - Child discount
  - Senior citizen discount

Advanced Features
  - Seat selection
  - Round trip booking
  - Weekend surcharge
  - Festival surcharge

Bus Type : Rate per KM
Non-AC : ₹2
AC : ₹3
Sleeper : ₹4

Start
│
├─ Enter Passenger Name
├─ Enter Age
├─ Enter Bus Type
├─ Enter Number of Tickets
├─ Enter Distance
├─ Enter Travel Day
│
├─ Age < 5?
│      └─ Yes → Free Ticket
│
├─ Age between 5 and 12?
│      └─ Yes → 50% Discount
│
├─ Else
│      └─ Full Fare
│
├─ Select Bus Type
│      ├─ AC → ₹3/km
│      ├─ Non-AC → ₹2/km
│      └─ Sleeper → ₹4/km
│
├─ Weekend?
│      └─ Yes → Add ₹100 surcharge
│
├─ Calculate Total Fare
│
├─ Generate Reservation Summary
│
└─ Display Final Amount
End

"""

# Passenger Name
# Passenger Age
# Bus Type (AC / Non-AC / Sleeper)
# Number of Tickets
# Travel Distance (km)
# Travel Day (Weekday / Weekend)

print("BUS RESERVATION SYSTEM \n")

passengers_name = input("Passengers Name: ")
passengers_age = int(input("Passengers Age: "))
passengers_bus_type = input("AC / NON-AC or Sleeper: ").upper()
number_of_tickets = int(input("Number of tickets: "))
travel_distance = float(input("Travel Distance: "))
travel_day = input("Travel Day: ")
print(f"Welcome, {passengers_name} to Bus Reservation System.\n")


if not passengers_name:
   print("Invalid Passengers Name.")
else:
    print(f"Passengers name: {passengers_name}")

if passengers_bus_type == "AC":
    print("AC")
elif  passengers_bus_type == "NON-AC":
    print("Non AC")
elif passengers_bus_type == "SLEEPER":
    print("Sleeper")
else:
    print("Invalid Bus Type.")

if passengers_age <= 0:
    print("Invalid Passengers Age.")
elif passengers_age >= 1:
    print(f"Passengers age: {passengers_age}.")

    if number_of_tickets <= 0:
        print("Invalid Ticket Count Selection. Please choose numbers above 1.")
    else:
        print("Tickets more than 1.")

else:
    print("ELSE.")

#   - Ticket quantity
#   - Fare calculation
#   - Reservation summary
