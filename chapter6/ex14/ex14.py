import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
data1= [32,37,35,30,39,40,35,33,34]
n1= len(data1)
mean1= meanSimple(data1,n1)

data2= [33,31,29,25,34,37,27,32,31]
n2= len(data2)
mean2= meanSimple(data2,n2)

m0 = 6
a= 0.05
q=1-a/2 
# --------------------------------
freqs, relFreq, cumFreqs, relCumFreq, mean, var1, std1, CV = freqOfValues(data1,n1)
freqs, relFreq, cumFreqs, relCumFreq, mean, var2, std2, CV = freqOfValues(data2,n2)

Sp = Sp(std1, n1, std2, n2)
z = ( mean1 - mean2 ) / ( Sp * math.sqrt(1/n1 + 1/n2) )
print ("t = " ,z)
t_crit = stats.t.ppf( 0.975, n1+n2-2)
print("t_crit", t_crit)
if z < t_crit:
    print("H0 is approved")
else:
    print("Ha is approved")
