import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
 
students = {14,12,6}
regions = {"A","B", "C"}

df=pd.DataFrame(students, index=["A","B", "C"])
print("\n",df)
# Actual answer--------------
sample = { "A" : [14], "B" : [12], "C" : [6]}
n= 32
df=pd.DataFrame(sample)
print("\n",df)

print("\nA", df.loc[0,"A"])
Pa= df.loc[0,"A"] / n # i
Pb= df.loc[0,"B"] / n # ii
Pc= df.loc[0,"C"] / n # iii
PaUPb= Pa + Pb # iv OR -> PaUPb= ( df.loc[0,"A"] + df.loc[0,"B"]) / n 

print("\nProbabilities : \n",
    "\nPa= ", Pa, 
    "\nPb= ", Pb,
    "\nPc= ",Pc )
print("\nPaUPb", PaUPb)