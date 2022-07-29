import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import median, variance
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 

sample = [10,15,8,17,22,12,5,3,32,14,2,48,
          24,18,5,9,16,14,28,2,7,8,11,43,
          16,4,27,34,43,15,22,6,18,25,7,39,
          13,18,11,24,1,4,20,1,6,3,16,33,
          27,8,2,3,49,5,17,26,0,4,23,28]

n = len(sample)
sample.sort()
bins=10
srange=(-0.5,49.5)
#answers (i)
k=k(n) #count of bins k
R=R(sample,n)
d=5
printStatsInfo(sample,n,k,R,d)

freqOfValues, relFreqOfValues, cumFreqOfValues, relCumFreqOfValues, mean, variance, std= freqOfValues(sample,n)
freqOfBins,edges, xi, varBins = freqOfBins(sample, n, bins, srange)
cumFreqStats, lowLimit, binSize, extraPoints = stats.cumfreq(sample, numbins = bins, defaultreallimits= srange)
relCumFreq = relCumFreq(sample,cumFreqStats)
#answers (iii)
meansimple = meanSimple(sample,n)
meanNp = np.mean(sample)
varStats=statistics.variance(sample) #2
medianNp=np.median(sample) #3
medianBins(sample,n,d,bins,srange)
modeStats=stats.mode(sample) #4
stdNp=np.std(sample) # wasn't asked
relFreqOfRange = relFreqOfRange(sample, 10,21)
#answers (ii) 
# cv = lambda sample: np.std(sample, ddof=1) / np.mean(sample) * 100
CV =  std / mean * 100
lessThan(sample, 10)
moreThan(sample,29)
# --------------------------------------------
printValues(cumFreqStats, lowLimit, binSize, extraPoints,
                 meanNp, varStats, medianNp, modeStats, stdNp, CV)
figureFreqs(sample, bins, srange, base=5)
