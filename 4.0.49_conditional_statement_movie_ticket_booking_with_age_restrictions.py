"""
Movie Ticket Booking with Age Restrictions

Start
│
├─ Enter Age
├─ Enter Movie Rating
│
├─ Is Rating = U?
│      └─ Yes → Allow Booking
│
├─ Is Rating = U/A 13+?
│      ├─ Age ≥ 13?
│      │      └─ Yes → Allow Booking
│      └─ No → Deny Booking
│
├─ Is Rating = U/A 16+?
│      ├─ Age ≥ 16?
│      │      └─ Yes → Allow Booking
│      └─ No → Deny Booking
│
├─ Is Rating = A?
│      ├─ Age ≥ 18?
│      │      └─ Yes → Allow Booking
│      └─ No → Deny Booking
│
└─ Otherwise → Invalid Rating
End
"""

print(f"Welcome to Python Cinemas")

print("Movie ratings should be in U, U/A - 18, U/A - 16, U/A - 13, A \n")
user_age = int(input("Enter the age: "))
movie_rating = input("Enter the rating of the movie: ").upper()
print(f"You chose {movie_rating}. \n")

if movie_rating == "U":
  print(f"This movie is rated as Universal and is allowed for all ages. Your ticket has been booked successfully.")

elif movie_rating == "U/A - 18":
  print(f"This movie is rated U/A - 18 and is allowed for ages 18 and above.")

  if user_age >= 18:
    print(f"You have successfully booked your ticket.")

  else:
    print("Booking Denied: Age Restriction")

elif movie_rating == "U/A - 16":
  print(f"This movie is rated U/A - 16 and is allowed for ages 16 and above.")

  if user_age >= 16:
    print(f"You have successfully booked your ticket.")

  else:
    print("Booking Denied: Age Restriction")

elif movie_rating == "U/A - 13":
  print(f"This movie is rated U/A - 13 and is allowed for ages 13 and above.")

  if user_age >= 13:
    print(f"You have successfully booked your ticket.")

  else:
    print("Booking Denied: Age Restriction")

else:
  print("Invalid Rating.")
