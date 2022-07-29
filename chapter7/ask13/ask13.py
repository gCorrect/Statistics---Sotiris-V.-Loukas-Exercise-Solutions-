import numpy as np
import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *

# data----------------------------
data1= np.array([67,81,57,68,67,69,66,77,54])
n1= len(data1)
mean1 = meanSimple(data1,n1)
var1= 2.5

data2= np.array([59,69,56,59,63,66,64,71,54])
n2= len(data2)
mean2 = meanSimple(data2,n1)
var2= 1.5

D= np.subtract(data1,data2)
print("D= ", D)
meanD= meanSimple(D,n1)
a= 0.05
q=1-a/2 
# --------------------------------
freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(D,n1)
print("----------------------")
t = t(meanD, 3, std, n1)

t_crit = stats.t.ppf( 0.95,n1-1 )
print("t_crit= ", t_crit)

if abs(t) < abs(t_crit) :
    print("H0 is approved")
else:
    print("Ha is approved")

t = t(meanD, 0, std, n1)

t_crit = stats.t.ppf( 0.95,n1-1 )
print("t_crit= ", t_crit)

if abs(t) < abs(t_crit) :
    print("H0 is approved")
else:
    print("Ha is approved")
print("----------------------")
