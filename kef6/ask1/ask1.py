import numpy as np
import scipy.stats
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *

n=16
mean=62
std=9
a = 0.05
q=1-a/2 
# ii
m0= 65

std_m= std_m(std, n)
print("(i) Std_m= ",std_m)
print("meanx = ",mean," Var_m= ", std_m * std_m )

print("(i) t_0.25,15 = ",scipy.stats.t.ppf(q=q,df=15))
confidence = 0.95
t_crit = np.float64(abs(scipy.stats.t.ppf( (1-confidence)/2,n-1) ).item() )
print("(i) t_crit", t_crit.astype(np.float64))

confidenceInterval(a, n, mean, std)
    
interval = scipy.stats.t.interval(0.95, 15, mean, std_m)
print("t 95% with interval() : ", interval)

# ii
t = t(mean, m0, std, n)
t_05_15 = scipy.stats.t.ppf(q=a,df=15)
print("(ii)t_0.5,15 = ", t_05_15)
if t > t_crit.astype(np.float64) :
    print("H0 is approved")
else:
    print("Ha is approved")




