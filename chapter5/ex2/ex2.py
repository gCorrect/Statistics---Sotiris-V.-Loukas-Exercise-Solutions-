import scipy.stats
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  

mean=15
std=12
n=36

std_m= std_m(std, n)
print("(i) Std_m= ",std_m)
print("meanx = ",mean," Var_m= ", std_m * std_m )

rv = scipy.stats.norm(mean, std_m)

P = rv.cdf(17) - rv.cdf(11)
print("(ii) P(11<=X<=17= ", P)

P = rv.cdf(18) - rv.cdf(12)
print("(iii) P(12<=X<=18= ", P)


