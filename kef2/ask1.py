import numpy as np
import matplotlib.pyplot as plt

n = 20
iq = np.array([85,88,124,92,105,110,75,107,90,115,94,100,99,96,98,100,103,114,102,104])
k=1+3.32*np.log(n)
#unsorted grouping
# group1 = [85,88,124,92]
# group2 = [105,110,75,107]
# group3 = [90,115,94,100]
# group4 = [99,96,98,100]
#group5 = [103,114,102,104]

# sorted grouping
group1 = [75,85,88,90]
group2 = [92,94,96,98]
group3 = [99,100,100,102]
group4 = [103,104,105,107]
group5 = [110,114,115,124]

iq.sort()
iqSorted = np.array([ 75,85,88,90,92,94,96,98,99,100,100,102,103,104,105,107,110,114,115,124])

#plot
plt.hist(iq)
plt.show()
#print
string="iq:"
print(string.iq)
