import scipy.stats
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
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



