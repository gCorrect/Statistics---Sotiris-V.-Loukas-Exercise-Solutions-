# είναι η άσκηση 6

import scipy.stats
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *

Pm = 3/8
Pk = 2/8
Pp = 3/8

cost = {Pm * 2, Pk * -1}
Ex = sum(cost)
print("Ex= ", Ex)