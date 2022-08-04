import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
data= [15,13,15,12,15,16,22,15,12]
n=len(data)
m0= 18

mean = meanSimple(data,n)
print("sum",sum(data))

freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data,n)
# (i)
print("\n(i)")
print("Std= ",std)
print("meanx = ",mean," Var= ", variance )

std_m= std_m(std, n)
print("Std_m= ",std_m)
print("meanx = ",mean," Var_m= ", std_m * std_m )

sem = stats.sem(data)
print("sem = ", sem)

confidenceInterval( .95, n-1, mean, std)
interval = stats.t.interval(0.95, 8, mean, std_m)
print("t 95% with interval() : ", interval)
# (ii)
print("(ii)")
t = t(mean, m0, std, n)
print("t = ", t)

confidence = 0.90
t_crit = stats.t.ppf( (1-confidence)/2,n-1) 
print("t_crit", t_crit.astype(np.float64))

if t > t_crit :
    print("H0 is approved")
else:
    print("Ha is approved")



