import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# toy data
# np.random.seed(1)
# sample = np.random.rand(100)
# sample = [85,88,124,92,105,110,75,107,90,115,94,100,99,96,98,100,103,114,102,104]
sample=  [75, 85, 88, 90, 92, 94, 96, 98, 99, 100, 100, 102, 103, 104, 105, 107, 110, 114, 115, 124]
# Quantile cut into 10 bins
# cuts = (pd.qcut(sample, [0.2,0.3,0.5])    # change arange to your liking
#           .value_counts().cumsum()
#        ) 
# print("cuts",cuts)
qcut=(pd.qcut(sample,  5)    # change arange to your liking
          .value_counts().cumsum()
    ) 

print("qcut", qcut)
print("qcut", qcut.index)
# print("arrange", arrange)
plt.plot([a.right for a in qcut.index], qcut, marker='x')
plt.show()
