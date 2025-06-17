# Day 6 – Maze Solver with turn_right() Abstraction
# Uses right-hand wall-following logic to solve the maze in Reeborg's World.
# Abstracts repeated right-turn logic into a reusable function for clarity and maintainability.
# Author: ifnidbi
# Date: 2025-06-09

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
