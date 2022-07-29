import pandas as pd
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 
data = { "employed" : [206,154], "unemployed" : [34,106],  }
gender = ["male" , "female"]

df = pd.DataFrame(data, index = gender)

print(df)

n = df.values.sum()

Pmale= P(df.loc["male"].sum(),n)
Punemployed= P(df["unemployed"].sum(),n)

print("\nn= ", n)
PmaleUnemployed = P(df.loc["male"].at["unemployed"], n)
PmaleUnionUnemployed = Pun( Pmale, Punemployed, PmaleUnemployed) 
PfemaleEmployed = P(df.loc["male"].at["employed"], n)

print("Pmale= ", Pmale)
print("Punemployed= ", Punemployed)
print("unemployed= ", df["unemployed"].sum())
print("PmaleUnemployed= ", PmaleUnemployed)
print("\n (i) PmaleUnionUnemployed= ", PmaleUnionUnemployed)
print("\n (ii) PfemaleEmployed= ", PfemaleEmployed)


