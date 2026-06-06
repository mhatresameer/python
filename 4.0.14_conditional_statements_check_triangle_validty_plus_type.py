# Level 3: Nested Conditions

"""
14. Triangle Validity + Type
Input three side lengths.
First check if a triangle is valid.
If valid, classify as:
Equilateral - all sides are equal
Isosceles - any 2 sides are equal
Scalene - none of the sides are equal
Use nested conditions.
"""

side_1 = int(input("Enter a number for first side of the triangle: "))
side_2 = int(input("Enter a number for second side of the triangle: "))
side_3 = int(input("Enter a number for third side of the triangle: "))

# check if all sides are positive - start
if side_1 > 0 and side_2 > 0 and side_3 > 0:
  print(f"All sides are positive. This is a triangle")

  # check if the triangle is "Equilateral" - all sides are equal, "Isosceles" - any 2 sides are equal, "Scalene" - none of the sides are equal - start
  if side_1 == side_2 == side_3:
    print(f"Equilateral Triangle.")
  elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print(f"Isosceles Triangle.")
  else:
    print(f"Scalene Triangle")
  # check if the triangle is "Equilateral" - all sides are equal, "Isosceles" - any 2 sides are equal, "Scalene" - none of the sides are equal - start

else:
  print(f"Not all sides are positive. Hence this is not a triangle.")
# check if all sides are positive - end
