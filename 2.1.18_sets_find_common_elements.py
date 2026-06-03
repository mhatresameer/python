# Level 7: Sets
"""
Find common elements:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
Expected: {3, 4}
"""

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# Expected: {3, 4}

print(a)
print(b)
# printing output to check

print(type(a))
print(type(b))
# printing type to check type

# using & operator
common_elements = a & b # using & in between both variables
print(common_elements)

# using .intersection() operation
common_elements_intersection = a.intersection(b) # using .intersection() operator
print(common_elements_intersection)
