# Level 3: Common Interview Questions
""" Exercise 9: Variable Memory Concept. What happens here?
x = 10
y = x
x = 20
print(y)
Explain why. """

x = 10 # x is assigned a value 10
y = x # y is another variable that is initialized with value of x that is 10
x = 20 # new variable z is declared with a value of 20
print(y)
# since y holds the vale of 10 it will print 10 and new variable holds value 20 which was assigned later. This is also called assignment by object reference.
