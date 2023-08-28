# 10 REM ****************************
# 20 REM ** Listeing 2.1           **
# 30 REM ** Simple, Deterministic, **
# 40 REM ** Forward-Chaining       **
# 50 REM ** EXPERT SYSTEM          **
# 60 REM ****************************
"""
Listeing 2.1
Simple, Deterministic, Forward-Chaining
EXPERT SYSTEM
"""

# 70 REM -- Inference Engine:
# 80 CLS: PRINT ,"EXPERT": PRINT ,"------"

##### Inference Engine #####
print("EXPERT")
print("------")

# 90 HYPOTHESES%=100: EVIDENCE%=4: REM the no. of different hypotheses and the no. of different items of evidence

HYPOTHESES: int = 100  # The number of different hypotheses
EVIDENCE: int = 4  # The number of different items of evidence

# 100 DIM POSSIBLE%(HYPOTHESES%) : REM set to 1 initially and 0 when hypothesis ruled out
# 110 DIM A$(HYPOTHESES%,EVIDENCE%) : REM answer submitted by user
# 120 DIM Q$(HYPOTHESES%,EVIDENCE%) : REM name of question
# 130 DIM R$(HYPOTHESES%,EVIDENCE%) : REM correct reply
# 140 DIM N$(HYPOTHESES%) : REM name of hypothesis

import numpy as np  # Imported for mapping BASIC arrays; TODO: Convert to more Pythonic data structures

POSSIBLE: np.ndarray = np.ones(
    HYPOTHESES, dtype=int
)  # Set to 1 initially and 0 when hypothesis ruled out
A_str: np.ndarray = np.empty(
    (HYPOTHESES, EVIDENCE), dtype=str
)  # Answer submitted by user
Q_str: np.ndarray = np.empty((HYPOTHESES, EVIDENCE), dtype=str)  # Name of question
R_str: np.ndarray = np.empty((HYPOTHESES, EVIDENCE), dtype=str)  # Correct reply
N_str: np.ndarray = np.empty(HYPOTHESES, dtype=str)  # Name of hypothesis

# 160 REM -- Read knowledge base into above arrays
# 170 RESTORE: COUNTER%=0
# 180 READ A$: IF A$="999" THEN GOTO 250
# 190 COUNTER%=COUNTER%+1: POSSIBLE%(COUNTER%)=1: N$(COUNTER%)=A$
# 200 FOR I%=1 TO EVIDENCE%: READ A$
# 210 FOR J%=1 to LEN(A$)
# 220 IF MID$(A$,J%,1)=" " THEN L%=J%: J%=LEN(A$): Q$(COUNTER%, I%)=LEFT$(A$,L%): R$(COUNTER%,I%)=RIGHT$(A$,LEN(A$)-L%)
# 230 NEXT J%
# 240 NEXT I%: GOTO 180: REM input loop
# 250 HYPOTHESES%=COUNTER%

##### Read knowledge base into above arrays #####
COUNTER: int = 0
last_data = False
with open("data.dat") as data_file:
    for line in data_file:
        data_line = iter(line.split(","))
        data = next(data_line).strip()
        if data == "999":
            last_data = True
            break
        COUNTER = COUNTER + 1
        POSSIBLE[COUNTER] = 1
        N_str[COUNTER] = data
        for I_idx in range(1, EVIDENCE + 1):
            data = next(data_line).strip()
            for J_idx in range(len(data)):
                if data[J_idx] == " ":
                    L_idx = J_idx
                    Q_str[COUNTER, I_idx] = data[:L_idx]
                    R_str[COUNTER, I_idx] = data[L_idx + 1 :]
HYPOTHESES = COUNTER

# 260 REM -- Start questioning user:
# 270 FOR COUNTER%=1 TO HYPOTHESES%
# 280 IF POSSIBLE%(COUNTER%)=0 THEN GOTO 540
# 290 FOR I%=1 TO EVIDENCE%: IF A$(COUNTER%,I%) <> "" THEN GOTO 500
# 300 PRINT: PRINT "What is ";Q$(COUNTER%,I%);" ?"
# 310 PRINT "(Possible replies are :"
# 320 FOR Q%=1 TO HYPOTHESES%: IF POSSIBLE%(Q%)=1 THEN PRINT SPC(20);R$(Q%,I%)
# 330 NEXT Q%
# 340 PRINT "or '*' for don't-care or '< x' or '> x' for ranges.)"
# 350 INPUT A$(COUNTER%,I%)

while True:
    ##### Start questioning user #####
    for COUNTER in range(1, HYPOTHESES + 1):
        if POSSIBLE[COUNTER] == 0:
            continue
        for I_idx in range(1, EVIDENCE + 1):
            if A_str[COUNTER, I_idx] != "":
                continue
            print()
            print("What is", Q_str[COUNTER, I_idx], "?")
            print("(Possible replies are :")
            for Q_idx in range(1, HYPOTHESES + 1):
                if POSSIBLE[Q_idx] == 1:
                    print(" " * 20, R_str[Q_idx, I_idx])
            print("or '*' for don't-care or '< x' or '> x' for ranges.)", end="")
            A_str[COUNTER, I_idx] = input(": ")

        # 360 REM -- Look for other questions this might also apply to:
        # 370 FOR Q%=COUNTER%+1 TO HYPOTHESES%
        # 380 FOR E%=1 to EVIDENCE%
        # 390 IF Q$(Q%,E%)=Q$(COUNTER,I%) THEN A$(Q%,E%)=A$(COUNTER%,I%)
        # 400 NEXT E%: NEXT Q%

        ##### Look for other questions this might also apply to #####
        for Q_idx in range(COUNTER + 1, HYPOTHESES + 1):
            for E_idx in range(1, EVIDENCE + 1):
                if Q_str[Q_idx, E_idx] == Q_str[COUNTER, I_idx]:
                    A_str[Q_idx, E_idx] = A_str[COUNTER, I_idx]

        # 410 REM -- Look for hypotheses that can be discounted due to this answer:
        # 420 FOR H%=1 TO HYPOTHESES%
        # 430 FOR E%=1 TO EVIDENCE%
        # 440 POSS%=POSSIBLE%(H%): GOSUB 1500: REM test reply against question
        # 450 IF POSS%<POSSIBLE%(H%) THEN PRINT: PRINT N$(H%);" is ruled out." PRINT "Would you like to know why (Y/N)";: INPUT A$: IF A$="y" OR A$="Y" THEN PRINT
        # 460 POSSIBLE%(H%)=POSS% : REM result of test routine
        # 470 NEXT E%: NEXT H%
        # 480 P%=0: FOR Q%=1 TO HYPOTHESES%: P%=P%+POSSIBLE%(Q%): NEXT Q%
        # 490 IF P%=0 THEN PRINT "No possibilites left!": I%=EVIDENCE%: COUNTER%=HYPOTHESES%
        # 500 NExT I%: REM on to next question

        ##### Look for hypotheses that can be discounted due to this answer #####
        for H_idx in range(1, HYPOTHESES + 1):
            for E_idx in range(1, EVIDENCE + 1):
                # Test reply against question
                POSS = POSSIBLE[H_idx]
                sub_1500()
                if POSS < POSSIBLE[H_idx]:
                    print()
                    print(N_str[H_idx], "is ruled out.")
                    print("Would you like to know why (Y/N)", end="")
                    A = input(": ")
                    if A == "y" or A == "Y":
                        print()
                    POSSIBLE[H_idx] = POSS

        # 510 REM -- Display any theories that match user's replies:
        # 520 IF POSSIBLE%(COUNTER%) THEN PRINT CHR$(7): PRINT N$(COUNTER%);" is possible.": PRINT "Would you like to know (Y/N)": INPUT A$: IF A$="y" OR A$="Y" THEN GOSUB 1200

        ##### Display any theories that match user's replies #####
        if POSSIBLE[COUNTER]:
            print("\a")
            print(N_str[COUNTER], "is possible.")
            print("Would you like to know (Y/N)", end="")
            A = input(": ")
            if A == "y" or A == "Y":
                sub_1200()

    # 530 REM -- Now try another theory
    # 540 NEXT COUNTER%
    # 550 PRINT: PRINT "Wold you like another run (Y/N) ";: INPUT A$
    # 560 IF A$="y" OR A$="Y" THEN GOSUB 1200
    # 570 IF A$="n" OR A$="N" THEN END
    # 580 GOTO 260: REM Loop back

    ##### Now try another theory #####
    # end of COUNTER loop

    print()
    print("Would you like another run (Y/N)", end="")
    A = input(": ")
    if A == "y" or A == "Y":
        sub_1200()
    if A == "n" or A == "N":
        exit()
    # end of infinite loop


# 1200 REM -- 'How' routine:
# 1210 PRINT: PRINT "It has :"
# 1220 FOR Q%=1 TO EVIDENCE%
# 1230 PRINT Q$(COUNTER%,Q%);" of ";R$(COUNTER%,Q%)
# 1240 NEXT Q%
# 1250 RETURN


def sub_1200():
    """'How' routine"""
    print()
    print("It has :")
    for Q_idx in range(1, EVIDENCE + 1):
        print(Q_str[COUNTER, Q_idx], "of", R_str[COUNTER, Q_idx])


# 1300 REM -- Re-initializing routine
# 1310 FOR H%=1 TO HYPOTHESES%
# 1320 FOR E%=1 TO EVIDENCE%
# 1330 A$(H%,E%)="": NEXT E%
# 1340 POSSIBLE%(H%)=1
# 1350 NEXT H%
# 1360 RETURN


def sub_1300():
    """Re-initializing routine"""
    for H_idx in range(1, HYPOTHESES + 1):
        for E_idx in range(1, EVIDENCE + 1):
            A_str[H_idx, E_idx] = ""
        POSSIBLE[H_idx] = 1


# 1500 REM -- Comparison routine (process of elimination)
# 1510 REM -- uses C$, vr, va
# 1520 IF POSS% = 0 THEN RETURN : REM already ruled out
# 1530 IF Q$(COUNTER%,I%) <> Q$(H%,E%) THEN RETURN : REM wrong question
# 1540 IF A$(COUNTER%,I%)="*" THEN RETURN : REM user doesn't care
# 1550 IF A$(COUNTER%,I%)=R$(H%,E%) THEN RETURN : REM exact match
# 1560 C$=LEFT$(A$(COUNTER%,I%),1)
# 1570 IF C$<>"<" AND C$<>">" THEN POSS%=0: RETURN : REM failed exact match
# 1580 REM -- Now try range tests:
# 1590 VR=VAL(R$(H%,E%)) : REM numeric value
# 1600 VA=VAL(MID$(A$(COUNTER%,I%),2)) : REM numeric input
# 1610 IF C$="<" AND VR < VA THEN RETURN
# 1620 IF C$=">" AND VR > VA THEN RETURN
# 1630 POSS%=0: REM failed all its chances!
# 1640 RETURN
# 1650 REM -- Allows user to say e.g. "<200" meaning under 200 etc.


def sub_1500():
    """Comparison routine (process of elimination)"""
    global POSS
    if POSS == 0:  # Already ruled out
        return
    if Q_str[COUNTER, I_idx] != Q_str[H_idx, E_idx]:  # Wrong question
        return
    if A_str[COUNTER, I_idx] == "*":  # User doesn't care
        return
    if A_str[COUNTER, I_idx] == R_str[H_idx, E_idx]:  # Exact match
        return
    C_str = A_str[COUNTER, I_idx][0]
    if C_str != "<" and C_str != ">":
        POSS = 0
        return  # Failed exact match

    ##### Now try range tests #####
    VR = float(R_str[H_idx, E_idx])  # Numeric value
    VA = float(A_str[COUNTER, I_idx][1:])  # Numeric input
    if C_str == "<" and VR < VA:
        return
    if C_str == ">" and VR > VA:
        return
    POSS = 0  # Failed all its chances!
    # Allows user to say e.g. "<200" meaning under 200 etc.
