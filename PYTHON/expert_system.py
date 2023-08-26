"""
Listing 2.1
Simple, deterministic, forward-chaining
Expert System
"""


def sub_1200():
    """'How' routine"""
    print()
    print("It has :")
    for Q_idx in range(EVIDENCE):
        print(f"{Q[counter][Q_idx]} of {R[counter][Q_idx]}")


def sub_1300():
    """Re-initializing routing"""
    for H_idx in range(HYPOTHESES):
        for E_idx in range(EVIDENCE):
            A[H_idx][E_idx] = ""
        POSSIBLE[H_idx] = True


def sub_1500():
    """
    Comparison routine (process of elimination)
    Uses C_str, vr, va
    """
    global POSS_idx
    # Already ruled out
    if POSS_idx == 0:
        return
    # Wrong question
    if Q[counter][I] != Q[H_idx][E_idx]:
        return
    # User doesn't care
    if A[counter][I] == "*":
        return
    # Exact match
    if A[counter][I] == R[H_idx][E_idx]:
        return
    C_str = A[counter][I][0]
    # Failed exact match
    if C_str != "<" and C_str != ">":
        POSS_idx = 0
        return
    # Now try range tests
    vr = int(R[H_idx][E_idx])  # numeric value
    va = int(A[counter][I][2:])  # numeric input
    # Allows user to say e.g. "<200" meaning under 200 etc.
    if C_str == "<" and vr < va:
        return
    if C_str == ">" and vr > va:
        return
    POSS_idx = 0  # Failed all its chances


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
COUNTER = 0
with open("data.dat") as datafile:
    # INPUT loop
    for (
        data
    ) in (
        datafile
    ):  # TODO: This needs to be fixed. READ reads in comma-separated data items
        COUNTER += 1
        N.append(data)
        for _ in range(EVIDENCE):
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
