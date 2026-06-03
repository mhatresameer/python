# Level 9: Junior Developer Interview Challenges

"""
Create a dictionary:
{
   "name": "Laptop",
   "price": 50000,
   "stock": 25
}
Increase stock by 10.
"""

user_laptop_info = {
   "name" : "Laptop",
   "price" : 50000,
   "stock" : 25
}

# user_laptop_info["stock"] = user_laptop_info["stock"] + 10
user_laptop_info["stock"] += 10
print(user_laptop_info)
