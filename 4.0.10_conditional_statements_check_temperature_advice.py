# Level 2: if / elif / else Chains

"""
10. Temperature Advice
Input temperature in Celsius.
Print:
Condition:Output:
< 0:Freezing
0–15:Cold
16–30:Comfortable
> 30:Hot
"""

temperature_check = int(input("Enter any number to check the temperature today."))

if temperature_check <= 0:
  print(f"{temperature_check} is at freezing point.")
elif temperature_check > 0 and temperature_check <= 15:
  print(f"{temperature_check} is at cold stage.")
elif temperature_check > 15 and temperature_check <=30:
  print(f"{temperature_check} is confortable and you can head outside.")
else:
  print(f"I don't know if you 😏 or the temperature outside at {temperature_check} is hot.")
