# Level 1: Arithmetic Operators

"""
Find Quotient and Remainder for user input number"
"""

num = int(input("Enter the number: "))
divisor = int(input("Enter the number for divisor with number: "))
"""
Find:
Quotient
Remainder
"""
quotient = num // divisor
remainder = num % divisor
print(f"The quotient for {num} / {divisor} is {quotient} and the remainder is {remainder}")
