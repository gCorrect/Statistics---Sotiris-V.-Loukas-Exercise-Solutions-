import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
mean = 42.5
m0 = 50
std=12
n=16
a = 0.05
q=0.95 
std_m= std_m(std,n)
# --------------------------------
print("\n(i)")
t = t(mean, m0, std, n)
t_crit = stats.t.ppf( 0.05,n-1) 
print("t_crit", t_crit)

if t > t_crit:
    print("H0 is approved")
else:
    print("Ha is approved")
# (ii)----------------------------
print("(ii)")
confidenceInterval( q=0.95, df=n-1, mean = mean, std = std)
interval = stats.t.interval(0.95,n-1, mean, std_m)
print("t 0.95% with interval() : ", interval)

