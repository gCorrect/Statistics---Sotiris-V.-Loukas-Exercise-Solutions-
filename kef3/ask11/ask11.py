import pandas as pd
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 
gender = { "boy" : [113,103,25,10], "girl" : [113,103,25,10] }
bloodGroup = ["0", "A", "B", "AB"]

df = pd.DataFrame(gender, index = bloodGroup)

print(df)

n = df.values.sum()

# Not Complete Exercise------------------------------------------------

# P5OrMore= P(df[">=5"].sum(),n)
# Patt= P(df.loc["attended"].sum(), n)

# Pinter5OrMoreAtt = P(df.loc["attended"].at[">=5"], n)
# indEvents= isIndependent(P5OrMore, Patt, Pinter5OrMoreAtt)

print("\nn= ", n)
# print("(i) Pgrade>=5= ", P5OrMore)
# print("(ii)Pinter5OrMoreAtt = ", Pinter5OrMoreAtt)

# print("Events independence: ", indEvents)




