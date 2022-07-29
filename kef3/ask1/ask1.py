import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import median, variance
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 

sample = [3,4,3,2,3,3,2,2,1,4,
          3,4,5,5,4,1,3,1,2,5]
n = len(sample)
sample.sort()
bins=5
srange=(0.5,5.5)
#answers (i)
k=k(n) #count of bins k
R=R(sample,n)
d=1
printStatsInfo(sample,n,k,R,d)

freqOfValues, relFreqOfValues, cumFreqOfValues, relCumFreqOfValues, mean, variance, std, CV= freqOfValues(sample,n)
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
relFreqOfRange = relFreqOfRange(sample, 1,3)
#answers (ii) 
# cv = lambda sample: np.std(sample, ddof=1) / np.mean(sample) * 100
CV =  std / mean * 100
lessThan(sample, 3)
moreThan(sample,4)
# --------------------------------------------
printValues(cumFreqStats, lowLimit, binSize, extraPoints,
                 meanNp, varStats, medianNp, modeStats, stdNp, CV)
figureFreqs(sample, bins, srange, base=0.5)
