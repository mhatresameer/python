# Level 4: Logical Operators

"""
age = 20
has_id = True
Write a condition that prints:
Allowed
only if:
Age is at least 18
Has valid ID
"""

user_age = int(input("Enter the age: "))
user_has_ID = True

user_allowed = user_age == 18 and user_has_ID is True
# try entering values above 18
print(f"The user is allowed only if {user_allowed}.")
