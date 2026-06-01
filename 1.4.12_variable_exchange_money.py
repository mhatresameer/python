# Level 4: Interview Coding Problems
""" Exercise 12: Exchange Money. """

user_money = int(input("Enter the money you have: "))

thousands = user_money // 1000 
hundreds = (user_money % 1000) // 100
tens = (user_money % 100) // 10
units = user_money % 10

print(thousands)
print(hundreds)
print(tens)
print(units)
