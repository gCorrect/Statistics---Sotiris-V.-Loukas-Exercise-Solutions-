import math
import statistics
import numpy as np
from pyparsing import srange
from scipy import stats
from statistics import median, variance
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  

# info
sample = [85,88,124,92,105,110,75,107,90,115,94,100,99,96,98,100,103,114,102,104]
n = len(sample)
sample.sort()
bins=5
srange=(74.5,124.5)
k=k(n) #count of bins k
R=R(sample,n)
d=d(R,k)
printStatsInfo(sample,n,k,R,d)

#answers (i) Find Frequencies, Relative Frequencies, Cumulative Frequencies, Relative Cumulative Frequencies
freqOfValues, relFreqOfValues, cumFreqOfValues, relCumFreqOfValues, mean, variance, std, CV= freqOfValues(sample,n)
freqOfBins,edges, xi, varBins = freqOfBins(sample, n, bins, srange)
cumFreqStats, lowLimit, binSize, extraPoints = stats.cumfreq(sample, numbins = bins, defaultreallimits= srange)
relCumFreq = relCumFreq(sample,cumFreqStats)
#answers (iii) Find mean, variance, median, mode, Percentage of pupils with iq between 85 -104
meansimple = meanSimple(sample,n)
meanNp = np.mean(sample)
varStats=statistics.variance(sample) #2
medianNp=np.median(sample) #3
medianBins(sample,n,d,bins,srange)
modeStats=stats.mode(sample) #4
stdNp=np.std(sample) # wasn't asked
relFreqOfRange = relFreqOfRange(sample, 85,104)
#  different CV
cv = lambda sample: np.std(sample, ddof=1) / np.mean(sample) * 100
cv = cv(sample)
print("cv lamda: ", cv)
CV =  std / mean * 100
# --------------------------------------------
printValues(cumFreqStats, lowLimit, binSize, extraPoints,
                 meanNp, varStats, medianNp, modeStats, stdNp, CV)
#answers(ii) Frequency Histograms
figureFreqs(sample, bins, srange, base=4)

