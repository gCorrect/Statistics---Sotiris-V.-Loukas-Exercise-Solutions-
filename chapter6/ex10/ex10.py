import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
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
print("\n(i)")
confidenceInterval(0.90, n-1, mean, std)

print("(ii)")
hypothesis( a, mean, m0, std,  n)
