"""
# Level 1: Basic if / else

1. Even or Odd
Take an integer as input.
Print Even if the number is divisible by 2, otherwise print Odd.

2. Positive, Negative, or Zero
Take a number as input and print exactly one of:
Positive
Negative
Zero

3. Voting Eligibility
Take age as input.
Print Eligible if age is at least 18, otherwise Not Eligible.

4. Largest of Two Numbers
Take two numbers and print the larger one.
Also handle the case where they are equal.

5. Pass or Fail
Take marks (0–100).
Print Pass if marks are at least 40, otherwise Fail.

# Level 2: if / elif / else Chains

6. Grade Calculator
Given marks:
Range:Grade
90–100:A
75–89:B
60–74:C
40–59:D
Below 40:F
Print the appropriate grade.
Bonus: print Invalid marks if input is outside 0–100.

7. Month Name
Input a number 1–12.
Print the corresponding month name using if/elif/else (not a dictionary yet).

8. Simple Calculator
Input:
first number
operator (+, -, *, /)
second number
Use if/elif/else to perform the operation.
Handle division by zero gracefully.

9. Traffic Light
Input color (red, yellow, green).
Print:
Color:Action
red:Stop
yellow:Wait
green:Go
anything else:Invalid signal

10. Temperature Advice
Input temperature in Celsius.
Print:
Condition:Output:
< 0:Freezing
0–15:Cold
16–30:Comfortable
> 30:Hot

# Level 3: Nested Conditions

11. ATM Withdrawal
Inputs:
balance
withdrawal amount
PIN correct? (True/False)
Rules:
PIN must be correct
Withdrawal must be positive
Balance must be sufficient
Print an appropriate message for each failure case.

12. Login Validation
Inputs:
username
password
Rules:
Username must not be empty
Password must be at least 8 characters
Only if both are valid, print Login accepted

13. Scholarship Eligibility
Inputs:
marks
family income
Eligible if:
marks ≥ 85
income ≤ 300000
Print Scholarship Eligible or Not Eligible.

14. Triangle Validity + Type
Input three side lengths.
First check if a triangle is valid.
If valid, classify as:
Equilateral
Isosceles
Scalene
Use nested conditions.

15. Discount Rules
Inputs:
cart total
premium member? (True/False)
Rules:
Premium + total ≥ 5000 → 20% discount
Premium + total < 5000 → 10% discount
Non-premium + total ≥ 5000 → 5% discount
Otherwise → no discount
Print the discount percentage.

# Level 4: Classic Interview Problems

16. Leap Year Checker
A year is a leap year if:
divisible by 400
or divisible by 4 but not by 100
Examples:
Year:Result
2024:Leap Year
1900:Not a Leap Year
2000:Leap Year

17. FizzBuzz (Conditionals Focus)
For numbers 1–30:
divisible by 3 → Fizz
divisible by 5 → Buzz
divisible by both → FizzBuzz
otherwise print the number
Key interview question: Why must the “both” condition come first?

18. Number of Digits
Input an integer and print whether it has:
1 digit
2 digits
3 digits
4+ digits
Do this using conditionals (no loops or strings yet).

19. BMI Category
Inputs: weight (kg), height (m).
Compute BMI:
BMI=
height
2
weight
Classify:
BMI:Category
< 18.5:Underweight
18.5–24.9:Normal
25–29.9:Overweight
≥ 30:Obese

20. Shipping Cost Calculator
Inputs:
weight in kg
distance in km
express shipping? (True/False)
Example rules:
Base charge = ₹50
+ ₹10 per kg
+ ₹2 per km if distance > 100 km
+ ₹100 if express
Print total shipping cost.

# Level 5: Output-Prediction Questions (Very Common in Interviews)

21. Predict the output
What prints and why?

22. Predict the output
What prints and why?

23. Predict the output
What prints and why?

24. Predict the output
What prints and why?

25. Predict the output
How many lines print? Why?

# Level 6: Edge Cases Interviewers Love

26. Marks Validation
Reject marks outside 0–100 before grading.
Ask yourself: should -5 be graded as F?

27. Division Safety
Why is this dangerous?
Write the conditional check that prevents division by zero.

28. Case-Insensitive Commands
Accept YES, Yes, yes, etc. as the same answer.
Hint: normalize the input first.

29. Multiple Conditions
Access is granted only if:
age ≥ 18
citizenship is Indian
membership is active
Write a single boolean expression for the condition.

30. Ordering Matters
Fix the bug:
Why does Excellent never print?

# Mini Mock Interview (5-minute drill)

Try to solve these without running Python:
What does if 0: do?
What does if "": do?

Why does if x % 15 == 0: usually appear before if x % 3 == 0: and if x % 5 == 0: in FizzBuzz?

What is wrong with if score > 90: elif score > 80: when score == 90?

Write a condition that is True only for numbers between 1 and 10 inclusive.
"""
