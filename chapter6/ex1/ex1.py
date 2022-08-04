import numpy as np
import scipy.stats
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
n=16
mean=62
std=9
a = 0.05
q=1-a
# ii
m0= 65
# --------------------------------
sem=std_m(std,n)
print_stat_values(mean,std*std,std,n,sem)
  #(i)
print("\n(i)")
confidenceInterval( q, n-1, mean, std)
interval = stats.t.interval(q, n-1, mean, sem)
print("Confidence Interval (t) of", q*100,"% with stats.t.interval() : ", interval)
  #(ii)
print("\n(ii)")
hypothesis(a,mean,m0,std,n)
