# import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
 
Pstats= 0.64
Ppsych= 0.56

PstatsPsych = Pind(Pstats, Ppsych)

print("PstatsPsych", PstatsPsych)
