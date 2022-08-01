import scipy.stats
import scipy.stats
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  

Pblack = 3/8
Pred = 2/8
Pgreen = 3/8

cost = {Pblack * 2, Pred * -1}
Ex = sum(cost)
print("Ex= ", Ex)
cost2= {Pblack*2*2, Pred} # multiply only costs not probabilities
Ex2= sum(cost2)
Varx = (Ex2 - Ex)*(Ex2 - Ex)
print("varx", Varx)

Varx = Ex2- (Ex*Ex)
print("varx", Varx)