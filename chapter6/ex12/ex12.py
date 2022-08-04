import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
n1= 10
mean1= 152
S1=23
std1=math.sqrt(S1)
n2= 10
mean2= 149
S2=37
std2=math.sqrt(S2)

m0 = 180
a= 0.05
q=1-a 
# --------------------------------
print("Hypothesis I : ")
print("(i)")
std12 = math.sqrt(S1/n1 + S2/n2) 
z_a2_df = stats.norm.ppf(q=0.975)
print("z_a2_df= ", z_a2_df) #<<<--------------
l= ( mean1 - mean2 ) - z_a2_df * std12
u= ( mean1 - mean2 ) + z_a2_df * std12
confidenceLevel = [l,u]
print("Confidence Interval (normal) of ",q," = ", confidenceLevel)

print("(ii)")
# t = t(mean, m0, std, n)
#
d0 = 0
z = ( mean1 - mean2 -d0 ) / std12
print ("t = " ,z)
t_crit = stats.norm.ppf( 0.95)
print("t_crit", t_crit)
if z < t_crit:
    print("H0 is approved")
else:
    print("Ha is approved")

# data----------------------------
n1= 10
mean1= 152
S1=20
std1=math.sqrt(S1)
n2= 10
mean2= 149
S2=30
std2=math.sqrt(S2)
# --------------------------------
print("Hypothesis II : ")
print("(i)")
Sp = Sp(std1, n1, std2, n2)
d0 = 0
z_a2_df =  stats.t.ppf( 0.975, n1+n2-2)
print("z_a2_df= ", z_a2_df) #<<<--------------
l = ( mean1 - mean2-d0 ) - z_a2_df* ( Sp * math.sqrt(1/n1 + 1/n2) )
u = ( mean1 - mean2-d0 ) + z_a2_df* ( Sp * math.sqrt(1/n1 + 1/n2) )
confidenceLevel = [l,u]
print("Confidence Interval (normal) of ",q," = ", confidenceLevel)

print("(ii)")
# t = t(mean, m0, std, n)
#
d0 = 0
z = ( mean1 - mean2 -d0 ) / ( Sp * math.sqrt(1/n1 + 1/n2) )
print ("t = " ,z)
t_crit = stats.t.ppf( 0.95, n1+n2-2)
print("t_crit", t_crit)
if z < t_crit:
    print("H0 is approved")
else:
    print("Ha is approved")


