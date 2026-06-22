"""
Ask the user for a number and print its table.
"""

# with FOR loop
user_table = int(input("Number for multiplication: "))

for count in range(1,11):
  answer = user_table * count
  print(f"{user_table} x {count} = {answer}")

# with WHILE loop
user_table = int(input("Number for multiplication: "))
count = 1

while count <= 10:
  answer = user_table * count
  print(f"{user_table} x {count} = {answer}")
  count += 1
