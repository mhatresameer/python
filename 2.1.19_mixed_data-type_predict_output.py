# Level 8: Mixed Data Type Interview Questions

"""
Predict output:
a = [1, 2, 3]
b = a
b.append(4)
print(a)
Why?
"""

a = [1, 2, 3]

# now b has the same value as a which is [1, 2, 3]
b = a

# b is appending another value in the list which is 4, so the output will be [1, 2, 3, 4]
b.append(4)

# since the value for b is pointing towards a at initial stage that means the updated value of b will be transferred to a
print(a)

# O/P: [1, 2, 3, 4]
