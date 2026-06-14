"""
Temperature Check
Input temperature.
35 → Hot
20–35 → Pleasant
< 20 → Cold
"""

check_temperature = float(input("Enter the temperature to check the severity: "))

if check_temperature >= 35:
  print("Its hot.")
elif check_temperature > 20 and check_temperature < 35:
  print("Pleasant.")
else:
  print("Cold.")
