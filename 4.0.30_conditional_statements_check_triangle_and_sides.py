"""
Triangle Validity + Type
Input three sides.
Check if triangle is valid.
If valid:
Equilateral
Isosceles
Scalene
"""

print(f"Program to check if the shape is triangle and its type.\n")

triangle_side_1 = int(input("Enter the first side of triangle: "))
triangle_side_2 = int(input("Enter the second side of triangle: "))
triangle_side_3 = int(input("Enter the third side of triangle: "))

# check triangle first - start
if triangle_side_1 > 0 and triangle_side_2 > 0 and triangle_side_3 > 0:
  # check sides of triangle first - start
  if triangle_side_1 + triangle_side_2 >= triangle_side_3:
    if triangle_side_2 + triangle_side_3 >= triangle_side_1:
      if triangle_side_1 + triangle_side_3 >= triangle_side_2:
        print("This is a triangle.\n")

        # check type - start
        if triangle_side_1 == triangle_side_2 == triangle_side_3:
          print("It's a Equilateral Triangle.")
        elif triangle_side_1 == triangle_side_2 or triangle_side_2 == triangle_side_3 or triangle_side_1 == triangle_side_3:
          print("It's a Isoceles Triangle.")
        else:
          print("It's a Scalene Triangle.")
        # check type - end

      else:
        print("Please fill all the sides to confirm the triangle and its type.")
    else:
      print("Please fill all the sides to confirm the triangle and its type.")
  else:
    print("Please fill all the sides to confirm the triangle and its type.")
  # check sides of triangle first - end

else:
  print("One or more side is zero. Not a triangle.")
# check triangle first - end
