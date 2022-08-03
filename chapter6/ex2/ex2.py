import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
data= [5,6,5,7,4,9,5,6,7]
n=len(data)
m0= 7

mean = meanSimple(data,n)
print("sum",sum(data))

freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data,n)
# (i)
print("(i) Std= ",std)
print("meanx = ",mean," Var= ", variance )

std_m= std_m(std, n)
print("Std_m= ",std_m)
print("meanx = ",mean," Var_m= ", std_m * std_m )

sem = stats.sem(data)
print("sem = ", sem)

t = t(mean, m0, std, n)

confidence = 0.95
t_crit = stats.t.ppf( (1-confidence)/2,n-1) 
print("t_crit", t_crit.astype(np.float64))

if t >  t_crit :
    print("H0 is approved")
else:
    print("Ha is approved")
# (ii)
interval = stats.t.interval(0.90, 8, mean, std_m)
print("(ii) t 90% with interval() : ", interval)
confidenceInterval(0.90, df=8, mean=mean, std=std)

