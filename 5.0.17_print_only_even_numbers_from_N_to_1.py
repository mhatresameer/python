# using WHILE loop
n = int(input("Enter a number: "))

while n >= 1:
    if n % 2 == 0:
        print(n)
    n -= 1


# using FOR loop
n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i)
