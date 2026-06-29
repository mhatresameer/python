num = int(input("Enter a number: "))

original_num = num
sum = 0

# Count the number of digits
digits = len(str(num))

while num > 0:
    digit = num % 10      # Get the last digit
    sum = sum + (digit ** digits)
    num = num // 10       # Remove the last digit

if sum == original_num:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is not an Armstrong number")
