# Day 4 – Rock Paper Scissors Game
# Simple text-based RPS game where the user plays against the computer.
# Uses random.randint, list indexing, and conditional logic.
# Author: ifnidbi
# Date: 2025-06-07

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

bot_move = random.randint(0,2)

player_move = int(input("Rock(0), Paper(1) or Scissors(2)?\n"))

moves = [rock, paper, scissors]

print(f"Your move:\n{moves[player_move]}")
print(f"Computer move:\n{moves[bot_move]}")

if player_move == bot_move:
    print("It's a draw!")
elif player_move == 0 and bot_move == 1:
    print("You lost.")
elif player_move == 1 and bot_move == 2:
    print("You lost.")
elif player_move == 2 and bot_move == 0:
    print("You lost")
else:
    print('You win!')
