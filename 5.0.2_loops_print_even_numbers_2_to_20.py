"""
Print even numbers from 2 to 20 taking user input.
"""

print("Print even numbers from 2 to 20 taking user input.\n")

start_num = int(input("Enter start number: "))
end_num = int(input("Enter last number: "))

while  start_num <= end_num:
  print(start_num)
  start_num += 2
