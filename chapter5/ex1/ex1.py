import scipy.stats
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  

mean=115
std=21
n=49

std_m= std_m(std, n)
print("(i) Std_m= ",std_m)
print("meanx = ",mean," Var_m= ", std_m * std_m )

rv = scipy.stats.norm(mean, std_m)

print("rv", rv)

P = rv.cdf(118) - rv.cdf(109)
print("(ii) P(109<=X<=118= ", P)



