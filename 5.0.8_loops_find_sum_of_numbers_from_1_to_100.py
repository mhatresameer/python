"""
Find the sum of numbers from 1 to 100.
"""

# with WHILE loop
num = 1
total = 0

while num <= 100:
  total += num
  num += 1

print(f"Sum: {total}")


# with FOR loop
total = 0

for num in range(0, 101):
  total += num

print(f"Sum: {total}")
