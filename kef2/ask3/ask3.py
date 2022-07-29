import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import median, variance
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 

sample = [17,14,10,17,14,12,11,15,9,16,8,14,14,12,14,14,13,
          12,15,12,6,12,7,10,8,14,10,11,8,12,12,10,16,15,6]
n = len(sample)
sample.sort()
bins=6
srange=(5.5,17.5)
#answers (i)
k=k(n) #count of bins k
R=R(sample,n)
d=d(R,k)
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
relFreqOfRange = relFreqOfRange(sample, 4.3,4.5)
#answers (ii) 
# cv = lambda sample: np.std(sample, ddof=1) / np.mean(sample) * 100
CV =  std / mean * 100
# --------------------------------------------
printValues(cumFreqStats, lowLimit, binSize, extraPoints,
                 meanNp, varStats, medianNp, modeStats, stdNp, CV)
figureFreqs(sample, bins, srange, base=3)
