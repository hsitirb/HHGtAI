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

while True:
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
            for Q_idx in range(HYPOTHESES):
                if POSSIBLE[Q_idx] == 1:
                    print(" " * 20, R[Q_idx][I])
            print("or '*' for don't care or '< x' or '> x' for ranges", end="")
            A[counter][I] = input(": ")
            ##### Look for other questions this might apply to: #####
            for Q_idx in range(counter, HYPOTHESES):
                for E_idx in range(EVIDENCE):
                    if Q[Q_idx][E_idx] == Q[counter][I]:
                        A[Q_idx][E_idx] = A[counter][I]
            ##### Look for hypotheses that can be discounted due to this answer #####
            for H_idx in range(HYPOTHESES):
                for E_idx in range(EVIDENCE):
                    POSS_idx = POSSIBLE[H_idx]
                    sub_1500()
                    if POSS_idx < POSSIBLE[H_idx]:
                        print()
                        print(N[H_idx], "is ruled out.")
                        print("Whould you like to know why?")
                        A_str = input("(Y/N)")
                        if A_str.upper() == "Y":
                            print()
                    POSSIBLE[H_idx] = POSS_idx  # Result of test routine
            P_idx = 0
            for Q_idx in range(HYPOTHESES):
                P_idx += POSSIBLE[Q_idx]
            if P_idx == 0:
                print("No possibilities left!")
                I = EVIDENCE  # TODO: This will not work - the loop variable will not be updated
                counter = HYPOTHESES  # TODO: This will not work - the loop variable will not be updated
            ##### On to the next question #####
        ##### Display any theories that match user's replies #####
        if POSSIBLE[counter]:
            print(f"{N[counter]} is possible.")
            print("Whould you like to know why?")
            A_str = input("(Y/N)")
            if A_str.upper() == "Y":
                sub_1200()
        ##### Now try another theory #####
    print()
    print("Would you like another run?")
    A_str = input("(Y/N)")
    if A_str.upper() == "Y":
        sub_1200()
    if A_str.upper() == "N":
        exit()
