import numpy as np
import matplotlib.pyplot as plt 

sample = ["A","K","A","K","K","K","K","K","A","K""A","K","A","K",
          "K","A","A","K","A","K","K","A","K","A","A","K","K","A"]

countA= sample.count("A")
print("countA: ", countA )

countK= sample.count("K")
print("countK: ", countK )

x = np.array(["A", "k"])
y = np.array([countA, countK])
# Plot
fig = plt.figure(figsize=(10, 10))
plt.bar(x, y, width=.5,  color='red', alpha=0.2)
plt.show()
