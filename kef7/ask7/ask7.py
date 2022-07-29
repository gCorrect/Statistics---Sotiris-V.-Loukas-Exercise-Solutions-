import numpy as np
import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
# data----------------------------
data = [10,11,13,11,10,11,10,11,12]
n = len(data)

m0 =10
a = 0.05
q=1-a/2 
# --------------------------------
freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data,n)
print("(i)")
print("mean= ", mean, ", Var= ", variance, ", std= ", std,",n= ", n )

std_m= std_m(std, n)
print("Std_m= ",std_m)
print("meanx= ",mean," Var_m= ", std_m * std_m )

sem = stats.sem(data)
print("sem= ", sem)    

t = t(mean, m0, std, n)

confidence = 0.95
t_crit = stats.t.ppf( 0.975,n-1 )
print("t_crit= ", t_crit)

confidenceInterval( .975, n-1, mean, std)
interval = stats.t.interval(0.95, n, mean, std_m)
print("t 95% with interval() : ", interval)

if abs(t) < abs(t_crit) :
    print("H0 is approved")
else:
    print("Ha is approved")



