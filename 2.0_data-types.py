# data-types : to assure what the value holds to avoid any erros.
# 4 types of data-types

# 1 - numeric data types
var_int = 5
var_float = 6.9
var_bool = True
var_complex = complex(8,3)

print(var_int)
print(var_float)
print(var_bool)
print(var_complex)
print("\n")

print(type(var_int))
print(type(var_float))
print(type(var_bool))
print(type(var_complex))
print("\n")

# 2 - string data types
username = "Python Data Types"
print(username)
print(type(username))
print("\n")

# 3 - sequence data types
# LIST - ordered collection of data seperated by commma and enclosed by square brackets. Lists are mutable and can be modified even after creation.
user_list = ["BMW", "Mercedes", "KIA", "Jaguar"]
print(user_list)
print(type(user_list))
print("\n")

# TUPLE - ordered collection of data seperated by commma and enclosed by round paranthesis. Tuples are immutable and cannot be modified after creation.
user_tuple = ("Honda", "Hyundai", "Suzuki", "Mazda")
print(user_tuple)
print(type(user_tuple))
print("\n")
