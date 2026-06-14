"""
Rock Paper Scissors
Input:
Player 1 choice
Player 2 choice
Determine winner using conditions.
"""

print("This is small program to play rock / papers and scissors game.")
print("Please ensure that R is for rock, P is for papers and S is for scissors.")
print("Anything not understood, watch POGO.\n")

user_1 = input("Enter your name: ")
user_2 = input("Enter your name: ")

player_1 = input(f"{user_1} is player 1 and should enter your choice to play. R/S/P: ")
player_2 = input(f"{user_2} is player 2 and should enter your choice to play. R/S/P: ")

if player_1 == player_2:
  print("Its a draw.")
  
elif player_1 == "R" and player_2 == "S":
  print(f"{user_1} wins.")
  
elif player_1 == "S" and player_2 == "P":
  print(f"{user_1} wins.")
  
elif player_1 == "P" and player_2 == "R":
  print(f"{user_1} wins.")
  
elif player_1 in ["R", "P", "S"] and player_2 in ["R", "P", "S"]:
  print(f"{user_2} wins.")
  
else:
  print("Invalid input.")
