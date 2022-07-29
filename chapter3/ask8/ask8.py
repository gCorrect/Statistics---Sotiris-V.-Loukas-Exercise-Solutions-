import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 
Pa= 0.15
Pm= 0.2
PaUnm= 0.25

PaInterm = Pa + Pm - PaUnm
PcondAM = Pcond(PaInterm, Pm)
indEvents= isIndependent(Pa, Pm, PaInterm)

print("\n(i) Pa_inter_m= ", PaInterm)
print("(ii) Pcond(a|m)= ", PcondAM)
print("(iii) Events independence: ", indEvents)


# print("Punemployed= ", Punemployed)
# print("unemployed= ", df["unemployed"].sum())
# print("PmaleUnemployed= ", PmaleUnemployed)
# print("\n (i) PmaleUnionUnemployed= ", PmaleUnionUnemployed)
# print("\n (ii) PfemaleEmployed= ", PfemaleEmployed)




