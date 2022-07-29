import pandas as pd
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *
 
data = { "didNotAttend" : [25,15], "attended" : [15,45],  }
performance = {"good" , "veryGood"}

df = pd.DataFrame(data, index = performance)

print(df)

data = { "good" : [25,15], "very good" : [15,45],  }
attendance = ["didntAttend" , "attended"]

df = pd.DataFrame(data, index = attendance)

print(df)
n= df["very good"].sum()+ df["good"].sum()

print("n= ", n)
Patt= P(df.loc["attended"].sum(),n)
Pverygood= P(df["very good"].sum(), n )
PattVerygood = P(df["very good"][1], n)
PcondVerygoodAtt = P( PattVerygood, Pverygood) 
indEvents= isIndependent(Patt, Pverygood, PattVerygood)

print("Patt= ", Patt)
print("Pverygood= ", Pverygood)
print("PattVerygood= ", PattVerygood)
print("P(Verygood | Att)= ", PcondVerygoodAtt)
print("Events independence: ", indEvents)
# att= df.loc["attended"].at["good"] + df.loc["attended"].at["very good"]

print("att= ", Patt)


