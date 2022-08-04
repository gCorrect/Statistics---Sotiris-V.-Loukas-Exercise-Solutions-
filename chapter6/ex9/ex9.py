import numpy as np
import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
data= [168,166,169,166,173,170,170,173,166,173,
        166,170,168,166,173,166,165,165,161,166]
n= len(data)
mean= meanSimple(data,n)
var= pow(5,2)
std= 5
m0 = 165
a= 0.05
q=1-a 
# --------------------------------
print("\n(i)")
confidenceIntervalNorm(q, n-1, mean, std)

print("(ii)")
hypothesis_norm( a, mean, m0, std,  n)
