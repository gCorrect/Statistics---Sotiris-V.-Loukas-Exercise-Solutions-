import numpy as np
import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
# data----------------------------
# normal distribution
mean = 42.5
m0 = 50
std=12
n=16
a = 0.05
q=1-a/2 
# --------------------------------
print("(i)")
t = t(mean, m0, std, n)
t_crit = stats.t.ppf( 0.95,n-1) 
print("t_crit", t_crit)

confidenceInterval( q=0.95, df=n-1, mean = mean, std = std)
if t == t_crit:
    print("H0 is approved")
else:
    print("Ha is approved")
# (ii)----------------------------
print("(ii)")
confidenceInterval( q=0.975, df=n-1, mean = mean, std = std)
interval = stats.norm.interval(0.95, mean, std)
print("norm 0.95% with interval() : ", interval)
interval = stats.norm.interval(0.975, mean, std)
print("norm 0.975% with interval() : ", interval)
interval = stats.t.interval(0.975, mean, std)
print("t 0.975% with interval() : ", interval)

interval = stats.norm.interval(0.025, mean, std)
print("norm 0.025% with interval() : ", interval)
interval = stats.t.interval(0.025, mean, std)
print("t 0.025% with interval() : ", interval)

z = stats.norm.cdf(3) - stats.norm.cdf(0) 
print("\n cdf(0<= z <=3", z)

