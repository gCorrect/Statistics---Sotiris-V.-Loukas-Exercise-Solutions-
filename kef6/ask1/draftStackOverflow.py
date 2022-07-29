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
m0= 65

confidence = 0.95

t = -1.333
# t1 = t(mean, m0, std, n)

t_crit = scipy.stats.t.ppf(q=a,df=15)
print("(ii)t_crit = ", t_crit)

if abs(t) < abs(t_crit) :
    print("H0 is approved")
else:
    print("Ha is approved")


