"""
Listing 2.1
Simple, deterministic, forward-chaining
Expert System
"""

##### Inference Engine #####
print("EXPERT")
print("------")


HYPOTHESES : int = 100  # The number of different hypotheses
EVIDENCE : int = 4      # The number of different items of evidence

POSSIBLE : list[bool] = [True] * HYPOTHESES  # Set to True initially, and False when the hypothesis is ruled out
A : list[list] = []                          # Answer submitted by user
Q : list[list] = []                          # Name of question
R : list[list] = []                          # Correct reply
N : list = []                                # Name of hypothesis
