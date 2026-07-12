# using WHILE loop
n = int(input("Enter a number: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i += 1

print("Sum =", total)


# using FOR loop
n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
