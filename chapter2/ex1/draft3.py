# source : https://stackoverflow.com/questions/59159444/cumulative-histogram-with-bins-in-frequency-python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sample=  [75, 85, 88, 90, 92, 94, 96, 98, 99, 100, 100, 102, 103, 104, 105, 107, 110, 114, 115, 124]
qcut=(pd.qcut(sample,  5)    # change arange to your liking
          .value_counts().cumsum()
    ) 

print("qcut", qcut)
print("qcut", qcut.index)
plt.plot([a.right for a in qcut.index], qcut, marker='x')
plt.show()
