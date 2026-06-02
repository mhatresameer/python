# Level 5: Mini Interview Challenge
""" Problem 4 - Without using any arithmetic operators (+, -, *, /), swap two variables. """

operator_1 = int(input("Enter first number: "))
operator_2 = int(input("Enter second number: "))

operator_1, operator_2 = operator_2, operator_1
print(f"After swapping the original number is {operator_1}")
print(f"After swapping the original number is {operator_2}")
