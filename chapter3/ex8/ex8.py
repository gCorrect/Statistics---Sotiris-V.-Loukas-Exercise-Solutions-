import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
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

