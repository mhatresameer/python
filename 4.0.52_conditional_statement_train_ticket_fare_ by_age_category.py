"""

Train Ticket Fare by Age Category :
  Basic
  1. Passenger Name (done)
  2. Passenger Age (done)
      - Infant (0–4 years)
      - Travels free of charge
      - Fare = ₹0
      - Child (5–12 years)
          50% of the standard fare
      - Adult (13–59 years)
          Full fare
      - Senior Citizen (60 years and above)
          30% discount on the standard fare
  Advanced
    3. First Class and Second Class fares
    4. AC and Non-AC coaches
    5. Student discounts
    6. Group booking discounts
    7. Dynamic pricing on weekends
    8. Return ticket discounts

"""

print("Python Express welcomes you aboard. \n")

print("Python Express offers below discounts and offers:")
print("For infants aging between 0 to 4, we have a zero fare.")
print("For children aging between 5 to 12, we have a 50% discount on the actual fare.")
print("For adults aging between 13 to 59, we offer a full fare to be paid.")
print("For senior citizens aged 60 and above are liable for a 30% discount on standard fare.\n")

print("STANDARD FARE : ₹500\n")

passenger_name = input("Passengers name: ")
passenger_age = int(input("Passengers age: "))

print("Thank you for choosing Python Express. \n")

if passenger_age < 0:
    print("Invalid Age detected. Please chose the right age.")

elif passenger_age >= 60:
    print("You fall under SENIOR CITIZEN category and are allowed for a 30% discount on your travel fare.")
    discount_30 = 500 * 0.30
    total_amount = 500 - discount_30
    print(f"Your ticket costs : ₹{total_amount}. Have a nice day ahead.")

elif passenger_age >= 13:
    print("You fall under ADULTS category and are allowed for a full fare.")
    total_amount = 500
    print(f"Your ticket costs : ₹{total_amount}. Have a nice day ahead.")

elif passenger_age >= 5:
    print("You fall under CHILDREN category and are allowed for a 50% discount on your travel fare.")
    discount_50 = 500 * 0.50
    total_amount = 500 - discount_50
    print(f"Your ticket costs : ₹{total_amount}. Have a nice day ahead.")

else:
    print(f"You fall under INFANTS category and are allowed for no cost.")
    print("Your ticket costs : ₹0. Have a nice day ahead.")
