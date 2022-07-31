# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# url = "https://gist.githubusercontent.com/operatorequals/ee5049677e7bbc97af2941d1d3f04ace/raw/e55fa867d3fb350f70b2897bb415f410027dd7e4"
# with httpimport.remote_repo(["hello"], url):
#     import hello
# hello.hello()

# import httpimport

# url = "https://gist.githubusercontent.com/operatorequals/ee5049677e7bbc97af2941d1d3f04ace/raw/e55fa867d3fb350f70b2897bb415f410027dd7e4"
# with httpimport.remote_repo(url):
#     import hello
# hello.hello()

# import urllib.request
# a = urllib.request.urlopen("https://gist.githubusercontent.com/operatorequals/ee5049677e7bbc97af2941d1d3f04ace/raw/e55fa867d3fb350f70b2897bb415f410027dd7e4")
# eval(a.read())

# hello()
# --------------------------------------------------------------
value=10
index=10
print("Less than: ",value, "is ", index+1)
# --------------------------------------------------------------
# arr1 = [3,4,2]
# arr2 = [1,7,9]
# ziparrays = zip(arr1,arr2)
# print("ziparrays", tuple(ziparrays))
# --------------------------------------------------------------
# import math
# from statistics import mean
# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt

# mul2Arrayes = lambda arr1,arr2 : [value1*value2 for value1,value2 in zip(arr1,arr2)]
# mul3Arrayes = lambda arr1,arr2,arr3 : [value1*value2*value3 for value1,value2,value3 in zip(arr1,arr2,arr3)]

# sample = [85,88,124,92,105,110,75,107,90,115,94,100,99,96,98,100,103,114,102,104]
# n = len(sample)
# sample.sort()
# bins=5
# srange=(74.5,124.5)
# cumFreq, lowLimit, binSize, extraPoints = stats.cumfreq(sample, numbins = bins, defaultreallimits= srange)

# fi,edges =np.histogram(sample,bins=bins, range= srange)
# print("fi",fi)
# print("edges",edges)

# print("cumFreq",cumFreq)
# for i in range(len(cumFreq)):
#     if (cumFreq[i] > n/2):
# # Li =edges[i]
#         median = edges[i] + 10* ( (n/2) - cumFreq[i-1] ) / fi[i] 
#         print("median",median)
#         break
# -------------------------------------------------------------
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
# ---------------------------------------------------------------
# # source : https://stackoverflow.com/questions/59159444/cumulative-histogram-with-bins-in-frequency-python
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# sample=  [75, 85, 88, 90, 92, 94, 96, 98, 99, 100, 100, 102, 103, 104, 105, 107, 110, 114, 115, 124]
# qcut=(pd.qcut(sample,  5)    # change arange to your liking
#           .value_counts().cumsum()
#     ) 

# print("qcut", qcut)
# print("qcut", qcut.index)
# plt.plot([a.right for a in qcut.index], qcut, marker='x')
# plt.show()
# -------------------------------------------------------------------
# # CumFreqQuant
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# # toy data
# # np.random.seed(1)
# # sample = np.random.rand(100)
# # sample = [85,88,124,92,105,110,75,107,90,115,94,100,99,96,98,100,103,114,102,104]
# sample=  [75, 85, 88, 90, 92, 94, 96, 98, 99, 100, 100, 102, 103, 104, 105, 107, 110, 114, 115, 124]
# # Quantile cut into 10 bins
# # cuts = (pd.qcut(sample, [0.2,0.3,0.5])    # change arange to your liking
# #           .value_counts().cumsum()
# #        ) 
# # print("cuts",cuts)
# qcut=(pd.qcut(sample,  5)    # change arange to your liking
#           .value_counts().cumsum()
#     ) 

# print("qcut", qcut)
# print("qcut", qcut.index)
# # print("arrange", arrange)
# plt.plot([a.right for a in qcut.index], qcut, marker='x')
# plt.show()
# --------------------------------------------------------------------
# return median
# fi,edges =np.histogram(sample,bins=bins, range= range)
# xi= midpoints=0.5*(edges[1:]+edges[:-1]) #edges[1:]-> second edges to end, edges[:-1] -> first edges to prefinal 
# mulxifi = mul2Arrayes(xi,fi)
# sum = sum(mulxifi)
# print("mulxifi:",mulxifi)
# print("sum:",sum)
# meanXifi = sum/n
# xi2fi = mul3Arrayes(xi,xi,fi)
# print("xi2fi", xi2fi)
# print("sumxi2fi", np.sum(xi2fi))

# variance =( 1/(n-1) ) *( np.sum(xi2fi) - (n*meanXifi*meanXifi) )
# print("variance", variance)

