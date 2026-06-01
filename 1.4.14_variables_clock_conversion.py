""" Exercise 14: Seconds Conversion """

user_time_conversion = int(input("Enter the time: "))
hours = user_time_conversion // 3600
minutes = (user_time_conversion % 3600) // 60
seconds = user_time_conversion % 60

print(hours)
print(minutes)
print(seconds)
