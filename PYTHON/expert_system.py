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
