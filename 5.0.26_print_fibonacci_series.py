# using FOR loop
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c


#using WHILE loop
n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")

    c = a + b
    a = b
    b = c

    count += 1
