# import pandas as pd
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 

# Actual answer--------------
sample = { "F" : [30], "B" : [24], "S" : [12], "G" : [9]}
n= 75
print("sample[F]",sample["F"][0])
# print("key f")
# print( 'F' in sample) / returns true or false

Pf= P(sample["F"][0], n) # i
Pb= P(sample["B"][0], n) # ii
Ps= P(sample["S"][0], n) # iii
Pg= P(sample["G"][0], n) # iii
# PaUPb= ( df[["A"]] + df[["B"]]) / n # WRONG
PsingleSport= Pun(Ps, Pg) # iv
PteamsSport= Pun(Pf,Pb)
PbInterTeamsSport = Pinter(Pb,PteamsSport)
PcondBTeamsSport = Pcond(Pb, PteamsSport)

print("\nPf= ", Pf, "\nPb= ", Pb, "\nPs= ",Ps, "\nPg= ",Pg )
print("\nPsingleSport= ", PsingleSport)
print("\nPteamsSport= ", PteamsSport)
print("\nPcondB_TeamsSport= ", PcondBTeamsSport)

# pandas--------------------
# students = {14,12,6}
# places = {"A","B", "C"}

# df=pd.DataFrame(sample)

# df=pd.DataFrame(students, index=["A","B", "C"])
# print(df)

# print("F", df[['F']])
# Pf= df[["F"]] / n # i
# Pb= df[["B"]] / n # ii
# Ps= df[["S"]] / n # iii
# Pg= df[["G"]] / n # iii
# # PaUPb= ( df[["A"]] + df[["B"]]) / n # WRONG
# PsingleSport= Ps + Pg # iv

# # PostP(B,teams)

# print("\nPf= ", Pf, "\nPb= ", Pb, "\nPs= ",Ps, "\nPg= ",Pg )
# print("\nPsingleSport", PsingleSport)

