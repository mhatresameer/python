"""
Hotel Room Booking Price Calculator

Start
│
├─ Enter Guest Name
├─ Enter Room Type
├─ Enter Number of Nights
│
├─ Nights < 1 ?
│      └─ Yes → Invalid Input
│
  ├─ Room Type = Standard ?
  │      └─ Cost = Nights × ₹2000
  │
  ├─ Else Room Type = Deluxe ?
  │      └─ Cost = Nights × ₹4000
  │
  ├─ Else Room Type = Suite ?
  │      └─ Cost = Nights × ₹7000
  │
  ├─ Else
  │      └─ Invalid Room Type
│
├─ Nights > 5 ?
│      └─ Apply 10% Discount
│
└─ Display Final Bill
End

Display:
  Guest Name
  Room Type
  Number of Nights
  Room Cost
  Discount Applied
  Final Amount Payable

"""

print("Python Hotel Room Booking.\n")

print("Python Stays offer current room costs: ")
print("STANDARD = ₹2000/night")
print("DELUXE = ₹4000/night")
print("SUITE = ₹7000/night.")
print("For 5 nights and above we offer 10% discount on final bill.\n")

guest_name = input("Enter the guest name: ")
room_type = input("Enter the room type you wish to choose: ").upper()
number_of_nights = int(input("Enter the number of nights you wish to stay with us: "))
print("Thank you for choosing Python Stays.\n")

if number_of_nights <= 0:
    print("Not valid nights, please choose a number to check availability. Have a nice day ahead.")

else:
    print(f"The number of nights you wish to stay with us : {number_of_nights}.")

    if room_type == "STANDARD":
        print(f"You chose {room_type} room type.")
        without_discount = number_of_nights * 2000
        print(f"As per {number_of_nights} nights, the total cost will be : {without_discount}.")

        if number_of_nights >= 5:
            print("You are eligible for a 10% discount.")
            with_discount = without_discount * 0.10
            total_bill = without_discount - with_discount
            print(f"The final bill with a 10% discount comes to be: {total_bill}.")

        else:
            print("You are not eligible for any discount.")

    elif room_type == "DELUXE":
        print(f"You chose {room_type} room type.")
        without_discount = number_of_nights * 4000
        print(f"As per {number_of_nights} nights, the total cost will be : {without_discount}.")

        if number_of_nights >= 5:
            print("You are eligible for a 10% discount.")
            with_discount = without_discount * 0.10
            total_bill = without_discount - with_discount
            print(f"The final bill with a 10% discount comes to be: {total_bill}.")

        else:
            print("You are not eligible for any discount.")

    elif room_type == "SUITE":
        print(f"You chose {room_type} room type.")
        without_discount = number_of_nights * 7000
        print(f"As per {number_of_nights} nights, the total cost will be : {without_discount}.")

        if number_of_nights >= 5:
            print("You are eligible for a 10% discount.")
            with_discount = without_discount * 0.10
            total_bill = without_discount - with_discount
            print(f"The final bill with a 10% discount comes to be: {total_bill}.")

        else:
            print("You are not eligible for any discount.")

    else:
        print("Please select valid room type.")
