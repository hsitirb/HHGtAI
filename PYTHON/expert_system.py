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
