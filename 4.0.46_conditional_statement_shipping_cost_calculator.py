"""
Shipping Cost Calculator
Input:
Weight
Distance
Rules:
Different shipping rates based on weight and distance ranges.
"""

print(f"Program to check shipping cost calculator.")
print(f"Please choose your shipping line from Maersk, CMA CGM, Hapag Llyod, Evergreen, ONE, MSC.")
print("Maersk - M, CMA CGM - C, Hapag Llyod - H, Evergreen - E, ONE - O, MSC - MSC \n")

ship_weight = float(input("Enter the weight of the ship (in kilograms): "))
ship_distance = float(input("Enter the distance covered by the ship (in kilometres): "))
ship_name = input("Enter the name of the ship you wish to check costing for: M/C/H/E/O/MSC: ")

if ship_name == "Maersk":
  weight = ship_weight * 10
  distance = ship_distance * 2
  total_maersk = weight + distance
  print(f"The rates for Maersk shipping as per new weight - {weight} and {distance:.2f} kilometers is {total_maersk}.")

elif ship_name == "CMA CGM":
  weight = ship_weight * 12
  distance = ship_distance * 1.5
  total_cma_cgm = weight + distance
  print(f"The rates for CMA CGM shipping as per new weight - {weight} and {distance:.2f} kilometers is {total_cma_cgm}.")

elif ship_name == "Hapag Llyod":
  weight = ship_weight * 15
  distance = ship_distance * 1.7
  total_hapag_llyod = weight + distance
  print(f"The rates for Hapag Llyod shipping as per new weight - {weight} and {distance:.2f} kilometers is {total_hapag_llyod}.")

elif ship_name == "Evergreen":
  weight = ship_weight * 9
  distance = ship_distance * 3
  total_evergreen = weight + distance
  print(f"The rates for Evergreen shipping as per new weight - {weight} and {distance:.2f} kilometers is {total_evergreen}.")

elif  ship_name == "ONE":
  weight = ship_weight * 5
  distance = ship_distance * 3.5
  total_one = weight + distance
  print(f"The rates for ONE shipping as per new weight - {weight} and {distance:.2f} kilometers is {total_one}.")

elif  ship_name == "MSC":
  weight = ship_weight * 10
  distance = ship_distance * 2.1
  total_msc = weight + distance
  print(f"The rates for MSC shipping as per new weight - {weight} and {distance:.2f} kilometers is {total_msc}.")

else:
  print("Not a valid shipping company in our database.")
