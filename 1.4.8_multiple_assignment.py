# Level 3: Common Interview Questions
""" Exercise 8: Multiple Assignment. Predict output: a, b, c = 1, 2, 3
a, b = b, a
print(a, b, c) """

a, b, c = 1, 2, 3

a, b = b, a
b, c = c, b

print(a)
print(b)
print(c)
