import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
 
numOfChildren = { "0" : [15,25,15], "1" : [27,37,20], "2" : [48,23,10], ">=3" : [40,15,9] }
edLevel = ["dim" , "lyk", "pan"]

df = pd.DataFrame(numOfChildren, index = edLevel)

print(df)

n = df.values.sum()

P3OrMore= P(df[">=3"].sum(),n)
Pdim= P(df.loc["dim"].sum(), n)
# Punemployed= P(df["unemployed"].sum(),n)

Pinter3OrMoreDim = P(df.loc["dim"].at[">=3"], n)
indEvents= isIndependent(P3OrMore, Pdim, Pinter3OrMoreDim)

print("\nn= ", n)
print("PnumOfChildren_>=3= ", P3OrMore)
print("Pdim= ", Pdim)
print("Pinter3OrMoreDim = ", Pinter3OrMoreDim)
print("Events independence: ", indEvents)




