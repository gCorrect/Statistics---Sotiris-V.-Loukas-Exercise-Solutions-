import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *

def freqs(array, n):
    freq=1
    xi=[]
    fi=[]
    freqs=[]
    relFreq=[]
    cumFreq=0
    cumFreqs=[]
    relCumFreq=[]
    for i in range(n-1):
        if (array[i+1] == array[i]):
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
        if (i==n-2 and array[i]==array[i+1]):    
            xi.append(array[i])
            fi.append(freq) 
            freqs.append([array[i],freq])
            relFreq.append((array[i],freq/n))
            cumFreq+=freq
            cumFreqs.append((array[i], cumFreq))
            relCumFreq.append((array[i],cumFreq/n))
            freq=1# Init freq to 1 for the next repetition to start counting
        elif (i==n-2 and array[i]!=array[i+1]): 
            xi.append(array[i+1])
            fi.append(1) 
            freqs.append([array[i+1],freq])
            relFreq.append((array[i+1],freq/n))
            cumFreq+=1
            cumFreqs.append((array[i+1], cumFreq))
            relCumFreq.append((array[i+1],cumFreq/n))        
    sumM=0
    for i in range(len(fi)):
        sumM = sumM + ( xi[i] * fi[i] )# Sum for -> mean
    mean = sumM/n
    # variance, standard deviation
    sumV=0
    sumV211=0
    sumStd=0
    Ex=0
    Ex2=0
    for i in range(len(fi)):
        sumV= sumV + ( xi[i] * xi[i] * fi[i] )# Σ(Xi^2*fi) -- (2.12)
        sumStd= sumStd + ( (xi[i]-mean)*(xi[i]-mean) )# Σ(Xi - Xmean)^2  
        sumV211= sumV211 + ( (xi[i]-mean)*(xi[i]-mean) )* fi[i]# Σ(Xi - Xmean)^2 -- (2.11)  
        Ex= Ex +  ( xi[i] * relFreq[i][1] ) # Ex= Σ(Xi*pi)
        Ex2= Ex2 +  ( xi[i] * xi[i] * relFreq[i][1] ) # Ex^2= Σ(Xi^2*pi)
    variance= 1/(n-1) * ( sumV- (n*mean*mean) ) # (2.12)
    v211= 1/(n-1) * (sumV211 ) # (2.11)
    std= math.sqrt( sumStd/(n-1) )
    varEx = Ex2- (Ex* Ex) # (4.9)
    CV= ( math.sqrt(variance)/mean ) *100
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
    print("V (211) = ", v211)
    print("VarEx= ", varEx) 
    print("\nstdOfValues", std)
    print("\nC.V= ", CV,"% \n")
    return freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV

# data----------------------------
data= [168,166,169,166,173,170,170,173,166,173,
        166,170,168,166,173,166,165,165,161,166]
n= len(data)
mean= meanSimple(data,n)
var= pow(5,2)
std= 5

freqs(data,n)


npArray= np.array([1,1,1,1,1])
print(npArray)

