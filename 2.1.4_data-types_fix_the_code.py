# Level 2: Type Conversion
""" Fix the code: """
# given code
"""
price = "100"
total = price + 50
print(total)
"""

# fixed code
price = "100"
price = int("100") # converting string into INT.
total = price + 50
print(total)
