"""
FizzBuzz (1-100)
if a number is divisible by 3 - its a Fizz
if a number is divisible by 5 - its a Buzz
if a number is divisible by both 3 and 5 - its a FizzBuzz
if none of the above applies - its a number self
"""

user_input = int(input("Enter a number to check the FizzBuzz game: "))

# always check the numbers probablity in both scenarios.
if user_input % 3 == 0 and user_input % 5 == 0:
  print("FizzBuzz")
elif user_input % 3 == 0:
  print("Fizz")
elif user_input % 5 == 0:
  print("Buzz")
else:
  print(f"{user_input}")
