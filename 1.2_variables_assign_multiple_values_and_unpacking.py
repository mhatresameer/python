# we can assign values to multiple variables.
assign1, assign2, assign3 = "Assigned Value 1", "Assigned Value 2", "Assigned Value 3"
print(assign1)
print(assign2)
print(assign3)

# one value to multiple variables.
assign4 = assign5 = assign6 = "Just one value for 3 different variables."
print(assign4)
print(assign5)
print(assign6)

# unpack a collection - its a list in this case
cars = ["BMW", "Mercedes", "KIA"]
print(cars)
print(type(cars))

bmw, mercedes, kia = cars
print(bmw)
print(mercedes)
print(kia)
