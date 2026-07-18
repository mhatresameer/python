# using FOR loop
num = int(input("Enter a number: "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")


# using WHILE loop
num = int(input("Enter a number: "))

total = 0
i = 1

while i < num:
    if num % i == 0:
        total += i
    i += 1

if total == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
