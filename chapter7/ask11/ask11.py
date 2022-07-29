import numpy as np
import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
# data----------------------------
n= 36
mean= 190
std= 24
m0 = 180
a= 0.01
q=1-a 
# --------------------------------
print("(i)")
confidenceIntervalNorm(0.90, n-1, mean, std)

print("(ii)")
t = t(mean, m0, std, n)
t_crit = stats.norm.ppf( 0.99, n-1)
print("t_crit", t_crit)
if t < t_crit:
    print("H0 is approved")
else:
    print("Ha is approved")
