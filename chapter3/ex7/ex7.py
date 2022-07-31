import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
 
data = { "employed" : [206,154], "unemployed" : [34,106],  }
gender = ["male" , "female"]

df = pd.DataFrame(data, index = gender)

print("\n",df)

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


