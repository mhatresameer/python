

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10          # Get the last digit
    reverse = reverse * 10 + digit
    num = num // 10           # Remove the last digit

print("Reversed number:", reverse)

"""
How it works
num % 10 extracts the last digit.
reverse = reverse * 10 + digit adds that digit to the reversed number.
num // 10 removes the last digit from the original number.
The loop continues until num becomes 0.

First iteration: reverse = 0 * 10 + 4 = 4
Second iteration: reverse = 4 * 10 + 3 = 43
Third iteration: reverse = 43 * 10 + 2 = 432
Fourth iteration: reverse = 432 * 10 + 1 = 4321

"""
