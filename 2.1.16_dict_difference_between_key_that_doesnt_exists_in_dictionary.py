# Level 6: Dictionaries
"""
Difference between:
student["salary"]
and
student.get("salary")
"""

student = {
   "name": "Sameer",
   "age": 28,
   "city": "Mumbai"
}

print(student)

# student["designation"]
"""
throws error as ErrorKey
"""

print(student.get("designation"))
# O/P: None
"""
student.get("salary") - this will check if the key exists and its value, if it doesnt (just in this case) it will show None as an output.
"""

# to add we can:
student["salary"] = 650000
print(student.get("salary"))

print(student)
