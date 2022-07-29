import math
import numpy as np
import scipy.stats as stats 

def t(mean, m0, std, n):
    t = ( mean-m0 ) / ( std / math.sqrt(n) )
    print("t= ", t)
    return ( mean-m0 ) / ( std / math.sqrt(n) )
# data----------------------------
data1= np.array([67,81,57,68,67,69,66,77,54])
n1= len(data1)
var1= 2.5

data2= np.array([59,69,56,59,63,66,64,71,54])
n2= len(data2)
var2= 1.5

D= np.subtract(data1,data2)
print("D= ", D)
meanD= 5
std=4.03
a= 0.05
q=1-a/2 
# --------------------------------
print("----------------------")
t = t(meanD, 3, std, n1)

t_crit = stats.t.ppf( 0.95,n1-1 )
print("t_crit= ", t_crit)

if abs(t) < abs(t_crit) :
    print("H0 is approved")
else:
    print("Ha is approved")

t = t(meanD, 0, std, n1)

t_crit = stats.t.ppf( 0.95,n1-1 )
print("t_crit= ", t_crit)

if abs(t) < abs(t_crit) :
    print("H0 is approved")
else:
    print("Ha is approved")
print("----------------------")
