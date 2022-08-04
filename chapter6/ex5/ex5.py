import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
mean_exp = 19.5 # experimentatl school
std_exp = 3
n_exp = 20
mean_pub = 18.8 # public shcool
std_pub = 1.5
n_pub = 15
a = 0.05
q=1-a/2 
# --------------------------------
print("\n(i)")
Sp = Sp(std_exp, n_exp, std_pub, n_pub)
d0 = 0
t = ( mean_exp - mean_pub -d0 ) / ( Sp * math.sqrt(1/n_exp + 1/n_pub) )
print ("t = " ,t)
t_crit = stats.t.ppf( 0.95, df= n_exp + n_pub -2) 
print("t_crit", t_crit)

if t < t_crit:
    print("H0 is approved")
else:
    print("Ha is approved")

