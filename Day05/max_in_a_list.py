# Day 5 – Highest Score Finder
# Iterates through a list of student scores and identifies the highest value.
# Uses a simple loop and comparison to avoid using built-in functions.
# Author: ifnidbi
# Date: 2025-06-08

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

highest_score = student_scores[0]

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)
