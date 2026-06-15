"""
Quadrant Checker
Input x and y coordinates.
Print:
Quadrant I
Quadrant II
Quadrant III
Quadrant IV
Origin
"""

coordinate_x = int(input("Enter the X co-ordinates: "))
coordinate_y = int(input("Enter the Y co-ordinates: "))

if coordinate_x == 0 and coordinate_y == 0:
  print("Origin")
  
elif coordinate_x > 0 and coordinate_y > 0:
  print("Quadrant I")
  
elif coordinate_x < 0 and coordinate_y > 0:
  print("Quadrant II")
  
elif coordinate_x < 0 and coordinate_y < 0:
  print("Quadrant III")
  
else:
  print("Quadrant IV")
