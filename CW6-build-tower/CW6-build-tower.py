# Submission.

def tower_builder(n_floors): 
    width = 2 * n_floors - 1
    return [("*" * floor).center(width, " ") for floor in range(1, width + 1, 2)]

"""
Code Review.

Strengths:
Deficiencies:
Remarks:
Solution:
"""


