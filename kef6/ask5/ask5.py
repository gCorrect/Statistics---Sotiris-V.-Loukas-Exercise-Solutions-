import numpy as np
import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
# data----------------------------
mean_exp = 19.5
std_exp = 3
n_exp = 20
mean_pub = 18.8
std_pub = 1.5
n_pub = 15
a = 0.05
q=1-a/2 
# --------------------------------
print("(i)")
Sp = Sp(std_exp, n_exp, std_pub, n_pub)
d0 = 0
t = ( mean_exp - mean_pub -d0 ) / ( Sp * math.sqrt(1/n_exp + 1/n_pub) )
print ("t = " ,t)
t_crit = stats.t.ppf( 0.95,n_exp + n_pub -2) 
print("t_crit", t_crit)

if t < t_crit:
    print("H0 is approved")
else:
    print("Ha is approved")

