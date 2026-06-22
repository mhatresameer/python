"""
Print all multiples of 3 from 1 to 30 using WHILE and FOR loop.
"""

# with WHILE loop
multiple_three = 1

while multiple_three <= 30:
  if multiple_three % 3 == 0:
    print(multiple_three)
  multiple_three += 1

# with FOR loop

for multiple_three in range(3, 31, 3):
  print(multiple_three)
