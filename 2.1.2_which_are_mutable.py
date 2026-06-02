# Level 1: Identify the Data Type
""" Exercise 2: Which of the following are mutable? list, tuple, dictionary, string, set. Explain why. """
# Mutable means an object can be changed after it is created.
# Immutable means it cannot be changed after it is created.

""" 01. List is mutable. Elements can be added, removed, or modified. """
fruits = ["Apple", "Banana", "Orange"]
print(fruits)
print(type(fruits))
# lets change the value of Orange with Guava
fruits[2] = "Guava"
print(f"The list is mutable and hence the value of Orange is replaced with Guava without changing the object {fruits}")

""" 02. Tuple	is immutable. Once created, its elements cannot be changed. """
cars = ("BMW", "KIA", "FIAT")
print(cars)
print(type(cars))
# lets try to change the value of FIAT with Mazda
cars[2] = "Mazda"
print(cars)
# it will throw an error stating - 'tuple' object does not support item assignment

""" 03. Dictionary is mutable. Key-value pairs can be added, updated, or deleted. """
user_info = {
    "name" : "Sameer",
    "age" : 30,
    "city" : "Mumbai"
}
# print(user_info)
# print(type(user_info))
user_info["age"] = 30.5
user_info["city"] = "Navi Mumbai"
print(user_info)
# check how to mutate the values properly

""" 04. String is not mutable. Characters cannot be changed in place. """
username = "Sameer"
# I want to replace the second e with E
username[4] = "E"
# it will throw an error stating - 'str' object does not support item assignment
username = "Sameer"
# username[4] = "E"
""" to make it mutable """
username = username[:4] + "E" + username[5:]
print(username)

""" 05. Set are mutable. Elements can be added or removed. """
user_sets = {1,2,3}
print(user_sets)
print(type(user_sets))
user_sets.add(4)
user_sets.remove(2)
print(user_sets)
