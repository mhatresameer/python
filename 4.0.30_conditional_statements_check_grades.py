"""
Grade Calculator
Input marks.
Marks
Grade
90+ : A
80-89 : B
70-79 : C
60-69 : D
Below 60 : F
"""

print("Program to print the grades.")
username = input("Enter your name: ")
marks = int(input("Enter the number to check your grades: "))

if marks >= 90:
  print(f"{username}, you have scored A grade.")
elif marks >= 80 and marks <= 89:
  print(f"{username}, you have scored B grade.")
elif marks >= 70 and marks <= 79:
  print(f"{username}, you have scored C grade.")
elif marks >= 60 and marks <= 69:
  print(f"{username}, you have scored D grade.")
else:
  print(f"{username}, we regret to inform you that you have recieved an F grade.")
