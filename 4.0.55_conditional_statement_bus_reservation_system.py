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
print("Bus Type Information:")
print("AC bus type offers ₹3/km")
print("Non-AC bus type offers ₹2/km")
print("Sleeper bus type offers ₹4/km\n")

passengers_name = input("Passengers Name: ")
passengers_age = int(input("Passengers Age: "))
passengers_bus_type = input("AC / NON-AC or Sleeper: ").upper()
number_of_tickets = int(input("Number of tickets: "))
distance_travelled = float(input("Travel Distance: "))
travel_day = input("Travel Day: ").upper()
print(f"Welcome, {passengers_name} to Bus Reservation System.\n")

print("Your detailed bill is here:")
print("============================")
if not passengers_name:
   print("Invalid Passengers Name.")
else:
    print(f"Passengers name: {passengers_name}")

if passengers_bus_type == "AC":
    passenger_bus_fare_per_km = 3
elif passengers_bus_type == "NON-AC":
    passenger_bus_fare_per_km = 2
elif passengers_bus_type == "SLEEPER":
    passenger_bus_fare_per_km = 4
else:
    print("Invalid Bus Type.")
    passenger_bus_fare_per_km = 0
    exit()

if travel_day in ["SATURDAY", "SUNDAY"]:
    weekend_surcharge = 100
else:
    print("Invalid choice.")
    weekend_surcharge = 0
    exit()


if passengers_age <= 0:
    print("Invalid Passengers Age.")
        
elif passengers_age < 5:
    print(f"You are eligible for a free ticket.")

elif 5 <= passengers_age <= 12:
    print(f"You are eligible for a 50% discount on your ticket.")

    if number_of_tickets <= 0:
        print("Invalid Ticket Count Selection. Please choose numbers above 1.")

    else:
        print(f"Number Of Tickets: {number_of_tickets}")

        print(f"Passengers Name: {passengers_name}")
        print(f"Passengers Age: {passengers_age}")
        print(f"Bus Type Selected: {passengers_bus_type}")
        print(f"Number Of Tickets: {number_of_tickets}")
        print(f"Travelling Distance: {distance_travelled}")
        print(f"Travel Day: {travel_day}")
        print(f"50% discount applied.")
        print(f"Weekend Surcharge: {weekend_surcharge}")

        final_bill = distance_travelled * passenger_bus_fare_per_km * number_of_tickets
        discount = (final_bill * 0.5)  + weekend_surcharge
        print(f"Discount applied. Your have to pay = {discount:.2f}. \n")

else:
    print("You have to pay full fare.\n")

    print(f"Passengers Name: {passengers_name}")
    print(f"Passengers Age: {passengers_age}")
    print(f"Bus Type Selected: {passengers_bus_type}")
    print(f"Number Of Tickets: {number_of_tickets}")
    print(f"Travelling Distance: {distance_travelled}")
    print(f"Travel Day: {travel_day}")
    print(f"Weekend Surcharge: {weekend_surcharge}")

    final_bill = distance_travelled * passenger_bus_fare_per_km * number_of_tickets + weekend_surcharge
    print(f"Your have to pay = {final_bill:.2f}")
