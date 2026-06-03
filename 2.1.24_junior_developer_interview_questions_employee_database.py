# Level 9: Junior Developer Interview Challenges
"""
Store details for 3 employees using:
List
Dictionary
String
Integer
Boolean
Example structure:
employees = [
   {
       "name": "Sameer",
       "age": 28,
       "active": True
   },
   {
       "name": "John",
       "age": 30,
       "active": False
   }
]
Print all active employees.
"""

# dictionary
employee_dict = [
    {
        "name" : "Sameer Mhatre",
        "age" : 30,
        "is_active_on_github" : True
    },
    {
        "name" : "Sagar Pawade",
        "age" : 39,
        "is_active_on_github" : False
    },
    {
        "name" : "Manoj Singh",
        "age" : 45,
        "is_active_on_github" : True
    },
    {
        "name" : "Imran Khan",
        "age" : 46,
        "is_active_on_github" : False
    }
]
print(employee_dict)
print(type(employee_dict))
