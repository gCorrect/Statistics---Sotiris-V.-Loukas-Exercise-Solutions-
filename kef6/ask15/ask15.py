import numpy as np
import scipy.stats as stats 
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
# data----------------------------
n1= 30
mean1= 18
std1=0.6
var1= pow(std1,2)

n2= 30
mean2= 17
std2= 0.5
var2= pow(std2,2)

a= 0.05
q=1-a/2 
# --------------------------------
print("(i)")
std12 = math.sqrt(var1/n1 + var2/n2) 
d0 = 0
z = ( mean1 - mean2 -d0 ) / std12
print ("t = " ,z)
z_crit = stats.norm.ppf( 0.975) 
print("z_crit", z_crit)

if z < z_crit:
    print("H0 is approved")
else:
    print("Ha is approved")

