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
  3. First Class and Second Class fares
  
  Advanced
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

print("STANDARD FARE : ₹500")
print("FIRST CLASS FARE : ₹1200")
print("SECOND CLASS FARE : ₹650\n")

passenger_name = input("Passengers name: ")
passenger_age = int(input("Passengers age: "))
passenger_class = input("Passengers class: ").upper()

print(f"Thank you for choosing Python Express, {passenger_name}. \n")

if passenger_age < 0:
    print("Invalid Age detected. Please chose the right age.")

elif passenger_age >= 60:

    if passenger_class == "STANDARD":
        discount_30 = 500 * 0.30
        total_amount = 500 - discount_30
        print(f"Passengers Name: {passenger_name}")
        print(f"Passengers Age: {passenger_age}")
        print(f"Passengers Class: {passenger_class}")
        print(f"Total cost: {total_amount:.2f}")

    elif passenger_class == "FIRST":
        discount_1200 = 1200 * 0.30
        first_class = 1200 - discount_1200
        print(f"Passengers Name: {passenger_name}")
        print(f"Passengers Age: {passenger_age}")
        print(f"Passengers Class: {passenger_class}")
        print(f"Total cost: {first_class:.2f}")

    elif passenger_class == "SECOND":
        discount_650 = 650 * 0.30
        second_class = 650 - discount_650
        print(f"Passengers Name: {passenger_name}")
        print(f"Passengers Age: {passenger_age}")
        print(f"Passengers Class: {passenger_class}")
        print(f"Total cost: {second_class:.2f}")

    else:
        print("Invalid class. \nChoose between FIRST, SECOND or STANDARD.")

elif passenger_age >= 13:

    if passenger_class == "STANDARD":
        total_amount = 500
        print(f"Passengers Name: {passenger_name}")
        print(f"Passengers Age: {passenger_age}")
        print(f"Passengers Class: {passenger_class}")
        print(f"Total cost: {total_amount:.2f}")

    elif passenger_class == "FIRST":
        total_amount = 1200
        print(f"Passengers Name: {passenger_name}")
        print(f"Passengers Age: {passenger_age}")
        print(f"Passengers Class: {passenger_class}")
        print(f"Total cost: {total_amount:.2f}")

    elif passenger_class == "SECOND":
        total_amount = 650
        print(f"Passengers Name: {passenger_name}")
        print(f"Passengers Age: {passenger_age}")
        print(f"Passengers Class: {passenger_class}")
        print(f"Total cost: {total_amount:.2f}")

    else:
        print("Invalid class. \nChoose between FIRST, SECOND or STANDARD.")

elif passenger_age >= 5:

    if passenger_class == "STANDARD":
        discount_50 = 500 * 0.50
        total_amount = 500 - discount_50
        print(f"Passengers Name: {passenger_name}")
        print(f"Passengers Age: {passenger_age}")
        print(f"Passengers Class: {passenger_class}")
        print(f"Total cost: {total_amount:.2f}")

    elif passenger_class == "FIRST":
        discount_1200 = 1200 * 0.50
        first_class = 1200 - discount_1200
        print(f"Passengers Name: {passenger_name}")
        print(f"Passengers Age: {passenger_age}")
        print(f"Passengers Class: {passenger_class}")
        print(f"Total cost: {first_class:.2f}")

    elif passenger_class == "SECOND":
        discount_650 = 650 * 0.50
        second_class = 650 - discount_650
        print(f"Passengers Name: {passenger_name}")
        print(f"Passengers Age: {passenger_age}")
        print(f"Passengers Class: {passenger_class}")
        print(f"Total cost: {second_class:.2f}")

    else:
        print("Invalid class. \nChoose between FIRST, SECOND or STANDARD.")

else:
    print(f"For infants aged 0 to 4, we offer free ride. Your ticket costs : ₹0. Have a nice day ahead.")
