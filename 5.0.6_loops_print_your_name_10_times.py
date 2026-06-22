"""
Print your name 10 times.
"""

# with WHILE loop
user_name = "Sameer"
count = 1

while count <= 10:
  print("Sameer")
  count += 1

# with FOR loop
for user_name in range(1, 11):
  print("Sameer")
  user_name += 1

# with IN-LINE numbers
for i in range(1, 11):
  print(f"{i}. Sameer")
  user_name += 1

# ONE-LINER using multiplication
user_name = "Sameer"
print(f"(user_name)\n" * 10)
