import math
from statistics import mean
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

mul2Arrayes = lambda arr1,arr2 : [value1*value2 for value1,value2 in zip(arr1,arr2)]
mul3Arrayes = lambda arr1,arr2,arr3 : [value1*value2*value3 for value1,value2,value3 in zip(arr1,arr2,arr3)]

sample = [85,88,124,92,105,110,75,107,90,115,94,100,99,96,98,100,103,114,102,104]
n = len(sample)
sample.sort()
bins=5
srange=(74.5,124.5)
cumFreq, lowLimit, binSize, extraPoints = stats.cumfreq(sample, numbins = bins, defaultreallimits= srange)

fi,edges =np.histogram(sample,bins=bins, range= srange)
print("fi",fi)
print("edges",edges)

print("cumFreq",cumFreq)
for i in range(len(cumFreq)):
    if (cumFreq[i] > n/2):
# Li =edges[i]
        median = edges[i] + 10* ( (n/2) - cumFreq[i-1] ) / fi[i] 
        print("median",median)
        break
return median
# fi,edges =np.histogram(sample,bins=bins, range= range)
# xi= midpoints=0.5*(edges[1:]+edges[:-1]) #edges[1:]-> second edges to end, edges[:-1] -> first edges to prefinal 
# mulxifi = mul2Arrayes(xi,fi)
# sum = sum(mulxifi)
# print("mulxifi:",mulxifi)
# print("sum:",sum)
# meanXifi = sum/n
# xi2fi = mul3Arrayes(xi,xi,fi)
# print("xi2fi", xi2fi)
# print("sumxi2fi", np.sum(xi2fi))

# variance =( 1/(n-1) ) *( np.sum(xi2fi) - (n*meanXifi*meanXifi) )
# print("variance", variance)

