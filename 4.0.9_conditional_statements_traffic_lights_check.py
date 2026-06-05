# Level 2: if / elif / else Chains

"""
9. Traffic Light
Input color (red, yellow, green).
Print:
Color:Action
red:Stop
yellow:Wait
green:Go
anything else:Invalid signal
"""

traffic_lights_check = input("Enter any of the three traffic signal colours (Red, Yellow, Green) to check the respective action: ")

if traffic_lights_check == "Red":
  print("STOP")
elif traffic_lights_check == "Yellow":
  print("WAIT")
elif traffic_lights_check == "Green":
  print("GO")
else:
  print("Invalid Signal")
