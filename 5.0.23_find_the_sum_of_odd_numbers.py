# using FOR loop
n = int(input("Enter the value of N: "))

sum = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        sum = sum + i

print("Sum of odd numbers =", sum)

# using WHILE loop
n = int(input("Enter the value of N: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum of odd numbers =", sum)
