# Level 9: Junior Developer Interview Challenges

"""
Find the last digit of a number.
Example:
num = 9876
Output: 6
"""

user_digit = int(input("Enter the number: "))

last_number = user_digit % 10
first_number = user_digit // 10

print(f"The last number from {user_digit} is {last_number}.")
print(f"The first number from {user_digit} is {first_number}.")
