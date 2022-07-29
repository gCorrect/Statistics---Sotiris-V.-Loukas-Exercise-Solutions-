import pandas as pd
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 
students = {14,12,6}
places = {"A","B", "C"}

df=pd.DataFrame(students, index=["A","B", "C"])
print(df)
# Actual answer--------------
sample = { "A" : [14], "B" : [12], "C" : [6]}
n= 32
df=pd.DataFrame(sample)

print("A", df[['A']])
Pa= df[["A"]] / n # i
Pb= df[["B"]] / n # ii
Pc= df[["C"]] / n # iii
# PaUPb= ( df[["A"]] + df[["B"]]) / n # WRONG
PaUPb= Pa + Pb # iv

print("\nPa= ", Pa, "\nPb= ", Pb, "\nPc= ",Pc )
print("\nPaUPb", PaUPb)