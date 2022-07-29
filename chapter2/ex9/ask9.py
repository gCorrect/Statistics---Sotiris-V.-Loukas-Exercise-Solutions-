import math
from re import A
import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import median, variance
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 

sample = ["A","K","A","K","K","K","K","K","A","K""A","K","A","K",
          "K","A","A","K","A","K","K","A","K","A","A","K","K","A"]

countA= sample.count("A")
print("countA: ", countA )

countK= sample.count("K")
print("countK: ", countK )

x = np.array(["A", "k"])
y = np.array([countA, countK])

# fig = plt.figure(figsize=(10, 10))
# frequencies = fig.plot()    
plt.bar(x, y, width=.5,  color='red', alpha=0.2)
plt.show()


# n = len(sample)
# # sample.sort()
# bins=5
# srange=(74.5,124.5)
# #answers (i)
# k=k(n) #count of bins k
# R=R(sample,n)
# d=10
# printStatsInfo(sample,n,k,R,d)

# freqOfValues, relFreqOfValues, cumFreqOfValues, relCumFreqOfValues, mean, variance, std= freqOfValues(sample,n)
# freqOfBins,edges, xi, varBins = freqOfBins(sample, n, bins, srange)
# cumFreqStats, lowLimit, binSize, extraPoints = stats.cumfreq(sample, numbins = bins, defaultreallimits= srange)
# relCumFreq = relCumFreq(sample,cumFreqStats)
# #answers (iii)
# meansimple = meanSimple(sample,n)
# meanNp = np.mean(sample)
# varStats=statistics.variance(sample) #2
# medianNp=np.median(sample) #3
# medianBins(sample,n,d,bins,srange)
# modeStats=stats.mode(sample) #4
# stdNp=np.std(sample) # wasn't asked
# relFreqOfRange = relFreqOfRange(sample, 95,104)
# #answers (ii) 
# # cv = lambda sample: np.std(sample, ddof=1) / np.mean(sample) * 100
# CV =  std / mean * 100
# # --------------------------------------------
# printValues(cumFreqStats, lowLimit, binSize, extraPoints,
#                  meanNp, varStats, medianNp, modeStats, stdNp, CV)
# figureFreqs(sample, bins, srange, base=10)
