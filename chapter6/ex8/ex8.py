import scipy.stats as stats 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
# data----------------------------
data1= [8,4,9,10,0,5,7,5,6]
n1= len(data1)
mean1 = meanSimple(data1,n1)
var1= 2.5

data2= [3,2,8,10,1,2,5,0,5]
n2= len(data2)
mean2 = meanSimple(data2,n1)
var2= 1.5

a= 0.05
q=1-a/2 
# --------------------------------
freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data1,n1)
freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data2,n2)

print("(i)")
std12 = math.sqrt(var1/n1 + var2/n2) 
d0 = 0
z = ( mean1 - mean2 -d0 ) / std12
print ("t = " ,z)
z_crit = stats.norm.ppf( 0.95) 
print("z_crit", z_crit)
if z < z_crit:
    print("H0 is approved")
else:
    print("Ha is approved")

print("(ii)")

t_a2_df = stats.norm.ppf(q=0.975)
print("t_a2_df", t_a2_df)
l = mean1 - mean2 - t_a2_df * std12
u = mean1 - mean2 + t_a2_df * std12
confidenceLevel = [l,u]
print("Confidence Interval (normal) of ",1-a," = ", confidenceLevel)
