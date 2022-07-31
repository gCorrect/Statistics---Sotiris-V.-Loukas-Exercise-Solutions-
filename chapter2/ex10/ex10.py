import statistics
import numpy as np
from scipy import stats
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
 

sample = [132,144,125,149,157,146,158,136,148,152,
          144,168,126,138,176,165,146,173,142,147,
          135,153,161,145,135,142,150,156,145,128,
          138,164,150,140,147,163,119,154,140,135]

n = len(sample)
sample.sort()
bins=6
srange=(118.5,178.5)
#answers (i)
k=k(n) #count of bins k
R=R(sample,n)
d=10
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
relFreqOfRange = relFreqOfRange(sample, 135,144)
#answers (ii) 
# cv = lambda sample: np.std(sample, ddof=1) / np.mean(sample) * 100
CV =  std / mean * 100
# --------------------------------------------
printValues(cumFreqStats, lowLimit, binSize, extraPoints,
                 meanNp, varStats, medianNp, modeStats, stdNp, CV)
figureFreqs(sample, bins, srange, base=10)
