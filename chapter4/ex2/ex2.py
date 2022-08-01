import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
 
# Poisson
x = 7
l = 5
P = Ppoisson(x, l)
print("(i) Ppoisson(X = 7)= ", P)

P = Ppoisson(10, l) + Ppoisson(11, l) + Ppoisson(12, l) + Ppoisson(13, l) + Ppoisson(14, l)   
print("(ii) Ppoisson(X>=10)= ", P)

P = Ppoisson(0, l)
print("(iii) Ppoisson= ", P)

P = Ppoisson(0, l) + Ppoisson(1, l) + Ppoisson(2, l) + Ppoisson(3, l) + Ppoisson(4, l)
print("(iv) Ppoisson(X<5)= ", P)