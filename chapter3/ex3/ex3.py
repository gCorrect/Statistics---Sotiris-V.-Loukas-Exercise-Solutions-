import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
 
# Actual answer--------------
sample = { "Football" : [30], "Basketball" : [24], "Swimming" : [12], "Athletics" : [9]}
n= 75
print("sample[Football]",sample["Football"][0])
# print("key f")
# print( 'F' in sample) / returns true or false

Pf= P(sample["Football"][0], n) # i
Pb= P(sample["Basketball"][0], n) # ii
Ps= P(sample["Swimming"][0], n) # iii
Pa= P(sample["Athletics"][0], n) # iii
# PaUPb= ( df[["A"]] + df[["B"]]) / n # WRONG
PsingleSport= Pun(Ps, Pa, 0) # iv
PteamsSport= Pun(Pf,Pb, 0)
Pinter_B_TeamsSport = Pinter(Pb,PteamsSport)
Pcond_B_TeamsSport = Pcond(Pb, PteamsSport)

print("\nPf= ", Pf, "\nPb= ", Pb, "\nPs= ",Ps, "\nPg= ",Pa )
print("\nPsingleSport= ", PsingleSport)
print("\nPteamsSport= ", PteamsSport)
print("\nPcondB_TeamsSport= ", Pcond_B_TeamsSport)
