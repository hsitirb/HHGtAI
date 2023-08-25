"""
Listing 2.1
Simple, deterministic, forward-chaining
Expert System
"""

##### Inference Engine #####
print("EXPERT")
print("------")


HYPOTHESES: int = 100  # The number of different hypotheses
EVIDENCE: int = 4  # The number of different items of evidence

# Set to True initially, and False when the hypothesis is ruled out
POSSIBLE: list[bool] = [True] * HYPOTHESES
A: list[list] = []  # Answer submitted by user
Q: list[list] = []  # Name of question
R: list[list] = []  # Correct reply
N: list = []  # Name of hypothesis


##### Read knowledge base into above lists #####
# TODO: Put data statements into data.dat
COUNTER = 0
with open("data.dat") as datafile:
    # INPUT loop
    while (data := datafile.readline()) != "999":
        COUNTER += 1
        N.append(data)
        for _ in range(EVIDENCE):
            data = datafile.readline()
            for J in range(len(data)):
                if data[J] == " ":
                    L = J
                    # TODO: Currently this will not work - the loop variable will not be updated
                    J = len(data)
                    Q[COUNTER].append(data[:L])
                    R[COUNTER].append(data[L + 1 :])

##### Start questioning user #####
for counter in range(HYPOTHESES):
    if POSSIBLE[counter] == 0:
        continue
    for I in range(EVIDENCE):
        if A[counter][I] == "":
            continue
        print()
        print(f"What is {Q[counter][I]}?")
        print("Possible replies are:")
        for Q in range(HYPOTHESES):
            if POSSIBLE[Q] == 1:
                print(" " * 20, R[Q][I])
        print("or '*' for don't care or '< x' or '> x' for ranges", end="")
        A[counter][I] = input(": ")
        ##### Look for other questions this might apply to: #####
        for Q in range(HYPOTHESES):