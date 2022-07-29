import numpy as np
import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
# data----------------------------
data= [3,10,5,4,7,8,9,9,8,5,5,8,6,6,9,10]
n= len(data)
mean= meanSimple(data,n)

m0 = 6
a= 0.05
q=1-a/2 
# --------------------------------
freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data,n)
variance= 4.5
std= 2.121
print("(i)")
confidenceInterval(0.90, n-1, mean, std)

print("(ii)")
t = t(mean, m0, std, n)
t_crit = stats.t.ppf( 0.95, n-1)
print("t_crit", t_crit)
if t < t_crit:
    print("H0 is approved")
else:
    print("Ha is approved")
