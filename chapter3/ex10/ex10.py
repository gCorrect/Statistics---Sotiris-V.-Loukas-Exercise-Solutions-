import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
 
grades = { "<5" : [40,10], ">=5" : [20,30] }
attendance = ["notAttended", "attended"]

df = pd.DataFrame(grades, index = attendance)

print(df)

n = df.values.sum()

P5OrMore= P(df[">=5"].sum(),n)
Patt= P(df.loc["attended"].sum(), n)

Pinter5OrMoreAtt = P(df.loc["attended"].at[">=5"], n)
indEvents= isIndependent(P5OrMore, Patt, Pinter5OrMoreAtt)

print("\nn= ", n)
print("(i) Pgrade>=5= ", P5OrMore)
print("(ii)Pinter5OrMoreAtt = ", Pinter5OrMoreAtt)

print("Events independence: ", indEvents)




