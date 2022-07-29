import scipy.stats
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *


rv = scipy.stats.norm(90, 20)
print("rv", rv)

P90 = rv.cdf(250) - rv.cdf(90) # 250 is my estimation for rare event thats tends to P = 0
print("(i) P(X>=90)= ", P)

P = rv.cdf(110) - rv.cdf(50)
print("(ii) P(50<=X<=110= ", P)

Pbin= Pbinomial(10,4, P90, 1-P90)
print("Pbinom=", Pbin)
