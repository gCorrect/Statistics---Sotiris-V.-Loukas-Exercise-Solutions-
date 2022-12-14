import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
data= [5,6,5,7,4,9,5,6,7]
n=len(data)
m0= 7
a= 0.05
q= 0.9
# --------------------------------
freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data,n)
sem = stats.sem(data)
print_stat_values(mean,variance,std,n,sem)
#answers--------------------------
#(i)
print("\n(i)")
hypothesis(a,mean,m0,std,n)
#(ii)
print("\n(ii)")
confidenceInterval( q, n-1, mean, std)
interval = stats.t.interval(q, n-1, mean, sem)
print("Confidence Interval (t) of", q*100,"% with stats.t.interval() : ", interval)


