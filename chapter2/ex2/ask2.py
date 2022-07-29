import math
import statistics
import numpy as np
from scipy import stats
from statistics import median, variance
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *

# info
sample = [4.2,4.4,4.4,4.3,4.2,4.4,4.8,4.9,4.4,4.2,3.8,4.2,4.4,
               4.3,4.5,4.8,4.7,4.2,4.2,4.8,4.5,3.6,4.1,4.3,3.9,4.2,
               4.0,4.5,4.4,4.1,4.0,4.0,3.8,4.6,4.9,3.8,4.3,4.3,3.9,
               3.9,4.0,4.2,4.3,4.7,4.1,4.0,4.6,4.4,4.6,4.4,4.9,4.4]
n = len(sample)
sample.sort()
srange=(3.55,4.95)
#answers (i)
k=k(n) #count of bins k
R=R(sample,n)
d=d(R,k)
printStatsInfo(sample,n,k,R,d)
bins=7

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
figureFreqs(sample, bins, srange, base=.2)
