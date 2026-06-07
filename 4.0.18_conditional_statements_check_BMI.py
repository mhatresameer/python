# Level 4: Classic Interview Problems

"""
19. BMI Category
Inputs: weight (kg), height (m).
Compute BMI:
BMI=
height
2
weight
Classify:
BMI:Category
< 18.5:Underweight
18.5–24.9:Normal
25–29.9:Overweight
≥ 30:Obese
"""

user_weight = float(input("Enter the weight in kilograms: "))
user_height = float(input("Enter the height in metres: "))

user_BMI = user_height/(user_weight**2)
print(f"{user_BMI} is good.")

# to be continued
