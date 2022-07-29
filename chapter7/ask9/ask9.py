import numpy as np
import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
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
q=1-a/2 
# --------------------------------
# freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data1,n1)
# freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data2,n2)

print("(i)")
confidenceIntervalNorm(0.975, n-1, mean, std)

print("(ii)")
z = t(mean, m0, std, n)
z_crit = stats.norm.ppf( 0.95)
print("z_crit", z_crit)
if z < z_crit:
    print("H0 is approved")
else:
    print("Ha is approved")

print("Hypothesis X~N(m,S^2), where var: unknown")
print("(i)")
freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV = freqOfValues(data,n)

k = k(n)
data.sort()
print("data= ", data)
R = R(data,n)
d= d(R,k)
srange=(161,173)
freqOfBins,edges, xi, varBins = freqOfBins(data, n, 5, srange)
print("now let's start. Most of the above are useless")
print(" following std and s are from the book")
std=3.37
print("(i)")
confidenceInterval(0.975, n-1, mean, std)

print("(ii)")
z = t(mean, m0, std, n)
z_crit = stats.t.ppf( 0.95, n-1)
print("z_crit", z_crit)
if z < z_crit:
    print("H0 is approved")
else:
    print("Ha is approved")

