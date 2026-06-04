# Level 3: Comparison Operators

"""
Take two numbers as input and print:
Equal or Not Equal
"""

user_comparision_input_1 = int(input("Enter the first number: "))
user_comparision_input_2 = int(input("Enter the second number: "))

# ==
equals_to = user_comparision_input_1 == user_comparision_input_2
# !=
not_equals_to = user_comparision_input_1 != user_comparision_input_2

print(f"When compare {user_comparision_input_1} with {user_comparision_input_2} it is {equals_to}")
print(f"When compare {user_comparision_input_1} with {user_comparision_input_2} it is not {not_equals_to}")
