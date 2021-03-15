rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

games = [rock, paper, scissors]



player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

if player_choice >=3 or player_choice <0:
  print("Invalid choice.")

else:
  print(games[player_choice])

  computer_choice = random.randint(0,2)
  print(f"Computer chose {games[computer_choice]}")

  if player_choice == 0 and computer_choice == 2:
    print("Player wins.")
  elif player_choice == 2 and computer_choice == 0:
    print("Computer wins.")
  elif player_choice > computer_choice:
    print("Player wins.")
  elif computer_choice > player_choice:
    print("Computer wins.")
  elif player_choice == computer_choice:
    print("Tie game.")
