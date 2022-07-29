import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos\TEI\mathimata\xrwstoumena\xeimerina\YpolNohm_2021_22\Eggrafa_709\books\stats_Loukas\exercises\functions')
from functions import *

n=5
x = 3
p=0.75 
q= 1- p

print("Combinator",possCombs(5,0))  
print("Pbinomial",Pbinomial(n, 0, p, q))  
  
print("Combinator",possCombs(5,1))  
print("Pbinomial",Pbinomial(n, 1, p, q))  

  
print("Combinator",possCombs(5,2))  
print("Pbinomial",Pbinomial(n, 2, p, q))  

print("P(<=2) ", Pbinomial(n, 0, p, q) + Pbinomial(n, 1, p, q) + Pbinomial(n, 2, p, q))  
