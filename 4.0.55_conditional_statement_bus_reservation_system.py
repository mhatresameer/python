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

print("BUS RESERVATION SYSTEM \n")

print("Bus Type Information:")
print("AC - ₹3/km")
print("Non-AC - ₹2/km")
print("Sleeper - ₹4/km\n")

print("Please note:")
print("Children aged from 5 to 12 are eligible for a 50% discount on their fare.")
print("Senior Citizen aged 60 and above are eligible for a 25% discount on their fare.\n")

print("Capacity of 40 Passengers in our bus.\n")

print("Seat Selection Charges:")
print("Window Seat charges ₹50 extra.")
print("Middle Seat charges ₹25 extra.")
print("Aisle Seat charges ₹10 extra.\n")

print("Enter your information below -")
passengers_name = input("Passengers Name: ")
passengers_age = int(input("Passengers Age: "))
passengers_bus_type = input("AC / NON-AC or Sleeper: ").upper()
passengers_number_of_tickets = int(input("Number of tickets: "))
passengers_seat_selection = input("Seat to be selected - Windows / Aisle or Middle: ").upper()
passengers_seat_number = int(input("Choose your seat between (1-50): "))
passengers_distance_travelled = float(input("Travel Distance: "))
passengers_travel_day = input("Travel Day: ").upper()
print(f"Welcome, {passengers_name} to Bus Reservation System.\n")

# passengers name validation - start
if not passengers_name.strip():
    print("Invalid Passengers Name.")
    exit()
# passengers name validation - end

# passengers bus type selection - start
if passengers_bus_type == "AC":
    passengers_bus_type_fare = 3
elif passengers_bus_type in ["NON-AC", "NON AC"]:
    passengers_bus_type_fare = 2
elif passengers_bus_type == "SLEEPER":
    passengers_bus_type_fare = 4
else:
    print("Invalid Input. Please select between AC, NON-AC and SLEEPER.")
    passengers_bus_type_fare = 0
    exit()
# passengers bus type selection - end

# passengers number of tickets check - start
if passengers_number_of_tickets <= 0:
    print("Invalid Selection. Tickets selected should be more than 0.")
    exit()
# passengers number of tickets check - end

# passengers distance travelled input - start
if passengers_distance_travelled <= 0:
    print("Input Invalid. The distance selected should be more 0.")
    exit()
# passengers distance travelled input - end

# passengers travel day selection - start
if passengers_travel_day in ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]:
    print("No Surcharge Applied.")
    passengers_weekend_surcharge = 0
elif passengers_travel_day in ["SATURDAY", "SUNDAY"]:
    print("Surcharge of ₹100 availed.")
    passengers_weekend_surcharge = 100
else:
    print("Invalid Inputs. Select a proper day.")
    passengers_weekend_surcharge = 0
    exit()
# passengers travel day selection - end

# passengers seat selection - start
if passengers_seat_selection == "WINDOWS":
    seat_selected = 50
elif passengers_seat_selection == "MIDDLE":
    seat_selected = 25
elif passengers_seat_selection == "AISLE":
    seat_selected = 0
else:
    print("Invalid Seat Selected.")
    exit()
# passengers seat selection - end

# passengers seat number - start
if 1 <= passengers_seat_number <= 40:
    print(f"{passengers_seat_number} seats booked successfully.")
else:
    print("Invalid seat number selection.")
    exit()
# passengers seat number - end

# total distance bill calculated - start
total_distance_bill = passengers_distance_travelled * passengers_bus_type_fare * passengers_number_of_tickets + seat_selected
# total distance bill calculated - end

# passengers age choices - start
if passengers_age <= 0:
    print("Invalid Age Selected.")
    exit()

elif passengers_age < 5:
    final_bill = 0
    print(f"You are eligible for a free ticket. Final Bill: {final_bill:.2f}")
    print("Have a safe journey.")

elif 5 <= passengers_age <= 12:
    final_bill =  (total_distance_bill * 0.5) + passengers_weekend_surcharge
    print(f"You are eligible for a 50% discount on your ticket. Final Bill: {final_bill:.2f}")
    print("Have a safe journey.")

elif 13 <= passengers_age <= 59:
    final_bill = total_distance_bill + passengers_weekend_surcharge
    print(f"Full fare applicable. Final Bill: {final_bill:.2f}")
    print("Have a safe journey.")

else:
    final_bill = (total_distance_bill * 0.75) + passengers_weekend_surcharge
    print(f"You are eligible for a 25% discount on your full fare. Final Bill: {final_bill:.2f}")
    print("Have a safe journey.")
# passengers age choices - end

# passengers reservation summary - start
print("\nBooking Summary:")
print(f"Passengers name: {passengers_name}")
print(f"Passengers age: {passengers_age}")
print(f"Bus type selected: {passengers_bus_type}")
print(f"Number of tickets: {passengers_number_of_tickets}")
print(f"Seat selected: {passengers_seat_selection} seat")
print(f"Seat numbers selected: {passengers_seat_number}")
print(f"Distance travelled: {passengers_distance_travelled:.2f} km")
print(f"Travel day: {passengers_travel_day}")
print(f"Final bill to pay: ₹{final_bill:.2f}")
# passengers reservation summary - end
