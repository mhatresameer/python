# Frequently Asked Operator Interview Questions

"""
1. Difference between / and //?
/ performs normal division and returns a float result.
// performs floor division and returns the quotient rounded down to the nearest whole number.
For example, 10 / 3 returns 3.3333333333333335, while 10 // 3 returns 3.

2. What does % return?
it returns the remainder for the sum.
For example, 17/5 returns 3 as quotient and 2 as remainder.

3. Difference between == and is?
== compares the value of both variables while is compares the value of pointer of 2 variables pointing at.

4. What is operator precedence?
its the order in which Python executes its mathematical operations.

B - Brackets
O - Orders (powers)
D - Division
M - Multiplication
A - Addition
S - Subtraction

  () Parentheses
  ** Exponent (power)
  *, /, //, %
  +, -
  Comparison operators (==, !=, >, <, >=, <=)
  not
  and
  or

5. What is short-circuiting in and and or?
Short-circuiting is an optimization used by Python with and and or. For and, if the first operand is False, Python stops because the result must be False.
For or, if the first operand is True, Python stops because the result must be True. This improves performance and can prevent errors by avoiding unnecessary evaluations.

6. Why is 10 == "10" False?
we cannot compare INT with strings.

7. When would you use % in real-world problems?
to check even-odd, to check visibility, find the last digit.

8. What is the difference between += and =?
+= adds the number to the original number while = just assigns the value to a variable.

9. What is the result of 5 and 0?
5 and 0 returns 0. In Python, the and operator returns the first falsy operand it encounters. Since 5 is truthy and 0 is falsy, the expression evaluates to 0.
It does not return False; it returns the actual operand 0.

10. Why does bool(0) return False?
it holds falsy or almost NULL value where zero has no holdings.
"""
