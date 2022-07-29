from scipy.stats import t 
import matplotlib.pyplot as plt 
import numpy as np 
     
n=16
mean=62
std=9

x = np.linspace(10, 110, 100) 
sf = t.sf(62,15, 62, 9)

# answers
print("sf", sf)
# Varying positional arguments 
y1 = t .pdf(x, 15, 62, 9) 
plt.plot(x, y1, "*")
plt.show() 