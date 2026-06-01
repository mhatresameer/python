# Level 1: Beginner (Understanding Variables)
""" Exercise 1: Create Variables
Create variables to store:
Your name
Age
City
Current job title
Print them in a single sentence. """
your_name = "Sameer"
your_age = 30
your_city = "Mumbai"
your_current_job_title = "Senior Engineer"
# expected o/p: My name is Sameer, I am 28 years old and I live in Panvel.
print(f"My name is {your_name}, I am {your_age} years old and I live in {your_city}")

# Exercise 2: Find the Data Type
# Without running the code, predict the output.
a = 10
b = 10.5
c = "10"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Exercise 3: Variable Reassignment
# What will be the final value of x?
x = 5
x = x + 3
x = x * 2
x = x - 4
print(x)
# answer is 12

# Exercise 4: Swap Two Variables
""" Swap the values without using a third variable.
a = 10
b = 20
Expected:
a = 20
b = 10 """
a = 10
b = 20
# use swap method
a, b = b, a
print(a)
print(b)

# Level 2: Input + Variables
""" Exercise 5: User Information
Take user's:
Name
Age
Print:
Hello Sameer, next year you will be 29 years old. """

username_input = input("Enter your name here: ")
username_age = int(input("Enter your name here: "))
username_age += 1

print(f"Hello {username_input}, next year you will be {username_age} years old.")

# Exercise 6: Rectangle Area
"""Take:
Length
Width
Store them in variables and calculate area.
Formula:
area = length * width"""
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area = length * width
print(float(area))
