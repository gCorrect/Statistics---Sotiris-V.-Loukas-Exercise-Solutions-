import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
n= 36
mean= 190
std= 24
m0 = 180
a= 0.01
q=1-a 
# --------------------------------
print("\n(i)")
confidenceIntervalNorm(0.90, n-1, mean, std)

print("(ii)")
hypothesis_norm( a, mean, m0, std,  n)
