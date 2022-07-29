import numpy as np
import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
# data----------------------------
data = [8,9,8,6,7,10,6,8,10]
n = len(data)

m0 =7
a = 0.05
q=1-a/2 
# --------------------------------
print("(i)")

mean = meanSimple(data,n)
print("sum",sum(data))

freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data,n)

print("(i) Std= ",std)
print("meanx = ",mean," Var= ", variance, "n", n )

std_m= std_m(std, n)
print("(i) Std_m= ",std_m)
print("meanx = ",mean," Var_m= ", std_m * std_m )

sem = stats.sem(data)
print("sem = ", sem)

t = t(mean, m0, std, n)
print("t = ", t)

confidence = 0.95
t_crit = np.float64(abs(stats.t.ppf( (1-confidence),n-1) ).item() )
print("(i) t_crit", t_crit.astype(np.float64))

confidenceInterval( .05, n, mean, std)
interval = stats.t.interval(0.95, 15, mean, std_m)
print("t 95% with interval() : ", interval)

if t > t_crit :
    print("H0 is approved")
else:
    print("Ha is approved")



