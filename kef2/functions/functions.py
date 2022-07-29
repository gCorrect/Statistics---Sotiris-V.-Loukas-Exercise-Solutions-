import math
import numpy as np
from statistics import variance
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats

def k(n):
    return 1+(3.322*math.log(n,10))
def R(sample, n):
    return sample[n-1]-sample[0]
def d(R,k):
    d= R/k
    if (d>1):
        d = int(R/k) + 1
    return  d
def freqOfValues(array, n):
    freq=1
    xi=[]
    fi=[]
    freqs=[]
    relFreq=[]
    cumFreq=0
    cumFreqs=[]
    relCumFreq=[]
    for i in range(n):
        if (array[i] == array[i-1]):
            freq+=1            
        else:
            xi.append(array[i])
            fi.append(freq) 
            freqs.append([array[i],freq])
            relFreq.append((array[i],freq/n))
            cumFreq+=freq
            cumFreqs.append((array[i], cumFreq))
            relCumFreq.append((array[i],cumFreq/n))
            freq=1# Init freq to 1 for the next repetition to start counting
    sumM=0
    for i in range(len(fi)):
        sumM = sumM + ( xi[i] * fi[i] )# Sum for -> mean
    mean = sumM/n
    # variance, standard deviation
    sumV=0
    sumStd=0
    for i in range(len(fi)):
        sumV= sumV + ( xi[i] * xi[i] * fi[i] )# Sum for -> variance
        sumStd= sumStd + ((xi[i]-mean)*(xi[i]-mean))
    variance= 1/(n-1) * ( sumV- (n*mean*mean) ) 
    std= math.sqrt( sumStd/(n-1) )
    # print
    print("\nValues: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nfreqOfValues=",freqs)
    print("\nrelFreqOfValues= ",relFreq)
    print("\ncumFreqOfValues= ",cumFreqs)
    print("\nrelCumFreqOfValues= ",relCumFreq)
    print("\nmeanOfValues= ", mean)
    print("\nvariancesOfValues=",variance)
    print("\nstdOfValues", std)

    return freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std
def freqOfBins(sample, n, bins, range):
    mul2Arrayes = lambda arr1,arr2 : [value1*value2 for value1,value2 in zip(arr1,arr2)]
    mul3Arrayes = lambda arr1,arr2,arr3 : [value1*value2*value3 for value1,value2,value3 in zip(arr1,arr2,arr3)]

    fi,edges =np.histogram(sample,bins=bins, range= range)
    xi= midpoints=0.5*(edges[1:]+edges[:-1]) #edges[1:]-> second edges to end, edges[:-1] -> first edges to prefinal 
    mulxifi = mul2Arrayes(xi,fi)
    meanxifi = sum(mulxifi)/n
    xi2fi = mul3Arrayes(xi,xi,fi)
    variance =( 1/(n-1) ) *( np.sum(xi2fi) - (n*meanxifi*meanxifi) )
    # v2
    v2 =( 1/(n-1) ) *( np.sum(mul2Arrayes(mul2Arrayes((xi - meanxifi),(xi - meanxifi)), fi)))   #2.9

    print("\nBins: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nfreqOfBins=",fi)
    print("\nedges= ",edges)
    print("\nxi= ", xi)
    print("\nmeanxifi= ", meanxifi)
    print("\nvariance", variance)
    print("\nv2", v2)

    return fi, edges, xi, variance
def relCumFreq(sample,cumFreq):
    relCumFreq = [(cumFreq/len(sample))]
    print("\nrelCumFreq: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nrelCumFreq=",relCumFreq)
    
    return relCumFreq
def meanSimple(sample,n):
    sum = 0
    for value in sample:
        sum= sum + value
    meanSimple= sum/n
    print("\nMeanSimple: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nmeanSimple=",meanSimple)
    return meanSimple
def medianBins(sample,n, d, bins, srange):
    cumFreq, lowLimit, binSize, extraPoints = stats.cumfreq(sample, numbins = bins, defaultreallimits= srange)

    fi,edges =np.histogram(sample,bins=bins, range= srange)
    print("fi",fi)
    print("edges",edges)

    print("cumFreq",cumFreq)
    for i in range(len(cumFreq)):
        if (cumFreq[i] > n/4):
    # Li =edges[i]
            F25 = edges[i] + d* ( (n/4) - cumFreq[i-1] ) / fi[i] 
            break
    for i in range(len(cumFreq)):
        if (cumFreq[i] > n/2):
    # Li =edges[i]
            median = edges[i] + d* ( (n/2) - cumFreq[i-1] ) / fi[i] 
            break
    for i in range(len(cumFreq)):
        if (cumFreq[i] > 3*n/4):
    # Li =edges[i]
            F75 = edges[i] + d* ( (3*n/4) - cumFreq[i-1] ) / fi[i] 
            break
    print("\nmedianBins: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nF25%= ", F25)
    print("\nmedianBins= ",median)
    print("\nF75%= ", F75)
    return median
def relFreqOfRange(array,start,end):
    f = 0
    for value in array:
        if value >= start and value <= end:
            f += 1
    relFreqOfRange = f/len(array)
    print("\nrelFreqOfRange: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nrelFreqOfRange=",relFreqOfRange)
   
    return relFreqOfRange
def figureFreqs(sample, bins, range, base):
    #res -> is for plotting cumulative histogram
    res = stats.cumfreq(sample, numbins=bins, defaultreallimits=range)
    x = res.lowerlimit + np.linspace(0, res.binsize*res.cumcount.size, res.cumcount.size)

    cumFreq, lowLimit, binSize, extraPoints = stats.cumfreq(sample, numbins = bins, defaultreallimits=range)
    
    #plot
    fig = plt.figure(figsize=(10, 10))
    histFreq = fig.add_subplot(2, 2, 1)
    histCumFreq = fig.add_subplot(2, 2, 2)
    histRelFreq = fig.add_subplot(2, 2, 3)
    histRelCumFreq = fig.add_subplot(2, 2, 4)
    # histFreq
    freqOfBins,edges, patches= histFreq.hist(sample,bins=bins, range= range, orientation='vertical',histtype='step', align='mid', edgecolor='k')
    histFreq.set_title('Frequency Histogram')
    midpoints=0.5*(edges[1:]+edges[:-1]) #edges[1:]-> second edges to end, edges[:-1] -> first edges to prefinal 
    histFreq.plot(midpoints,freqOfBins)# polygon
    loc = ticker.MultipleLocator(base=base) # this locator puts ticks at regular intervals
    histFreq.xaxis.set_major_locator(loc)
    # histCumFreq
    # histCumFreq.bar(x, res.cumcount, width=res.binsize, color='red')
    cumFreqOfBins, edges1, patches1 = histCumFreq.hist(sample,bins=bins, range= range, cumulative=True, orientation='vertical',histtype='step', align='mid', edgecolor='k')
    histCumFreq.set_title('Cumulative Histogram')
    histCumFreq.set_xlim([x.min(), x.max()])
    polPoints=(edges[1:]) #edges[1:]-> second edges to end, edges[:-1] -> first edges to prefinal 
    histCumFreq.plot(polPoints, cumFreq)#polygon
    loc = ticker.MultipleLocator(base=base) # this locator puts ticks at regular intervals
    histCumFreq.xaxis.set_major_locator(loc)
    # histRelFreq
    relFreqOfBins, edges1, patches1 = histRelFreq.hist(sample,bins=bins, range= range, density=True, orientation='vertical',histtype='step', align='mid', edgecolor='k')
    histRelFreq.set_title('Relative Frequency Histogram')
    histRelFreq.plot(midpoints, relFreqOfBins)# polygon
    # histRelCumFreq
    # histRelCumFreq.bar(x, res.cumcount/20, width=res.binsize, color='red', alpha=0.2)
    relCumFreqOfBins, edges1, patches1 = histRelCumFreq.hist(sample,bins=bins, range= range,density=True, cumulative=True, orientation='vertical',histtype='step', align='mid', edgecolor='k')
    histRelCumFreq.set_title(' Relative Cumulative Histogram')
    histRelCumFreq.set_xlim([x.min(), x.max()])
    histRelCumFreq.plot(polPoints, cumFreq/len(sample))# polygon
    plt.show()
def lessThan(sample, value):
    count=0
    for i in range(len(sample)):
        if (sample[i] < value):
            count+=1
        else: 
            break    
    print("\nLess Than :")
    print("---------------------------------------")
    print("---------------------------------------")
    print("Less than: ",value, "is ", count)
def moreThan(sample, value):
    count=0
    for i in range(len(sample)):
        if (sample[i] > value):
            count+=1    
    print("\nMore Than :")
    print("---------------------------------------")
    print("---------------------------------------")
    print("More than: ",value, "is ", count)
def printValues( cumFreqStats, lowLimit, binSize, extraPoints,
                 meanNp, varStats, medianNp, modeStats, stdNp, CV):
    print("\nprintValues:")
    print("---------------------------------------")
    print("---------------------------------------")
    print ("\ncumulative frequency (statistcs) : ", cumFreqStats)
    print ("Lower Limit : ", lowLimit)
    print ("bin size : ", binSize)
    print ("extra-points : ", extraPoints)
    # print ("res.binsize : ", res.binsize)
    # print ("res cumcount : ", res.cumcount)
    # print ("res cumcount.size : ", res.cumcount.size)
    # # print ("np.lispace : ", np.linspace(0, res.binsize*res.cumcount.size, res.cumcount.size))

    notation="meanNp= "
    print(notation,meanNp)
    
    notation="statistics.variance= "
    print(notation,varStats)

    notation="medianNp= "
    print(notation, medianNp)
    
    notation="modeStats= "
    print(notation,modeStats)
    
    notation="stdNp= "
    print(notation,stdNp)

    print("CV: ", CV)
def printStatsInfo(sample, n, k, R, d,):
    # stats info
    print("----stats info----")

    print("\nn=", n)
    notation="sample= "
    print(notation,sample)

    notation="k= "
    print(notation,k)

    notation="R= "
    print(notation,R)

    notation="d= "
    print(notation,d)

# functions---------------------------------------------------------
# fi function
def frequency(data, bins):
    # work with local sorted copy of bins for performance
    bins = bins[:]
    bins.sort()
    freqs = [0] * (len(bins)+1)
    for item in data:
        for i, bin_val in enumerate(bins):
            if item <= bin_val:
                freqs[i] += 1
                break
        else:
            freqs[len(bins)] += 1
    return freqs

# Python program to count the frequency of
# elements in a list using a dictionary 
def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% d : % d"%(key, value)) 
# Driver function
if __name__ == "__main__":
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
 
    CountFrequency(my_list)

#freq of specified range. From stackOF answers. I don'to use it
def freq(arr, min_n, max_n):
    return (
        len(arr) -
        next((j for j in range(len(arr)) if arr[j] >= min_n), len(arr)) - #next returns the next item in an iterator #len(arr) is default of next()
        next((j for j in range(len(arr)) if arr[len(arr) - j - 1] <= max_n), len(arr)) 
    ) / len(arr)