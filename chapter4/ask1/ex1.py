import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  

n=5
x = 3
p=0.75 
q= 1- p

print("Combinator",Pcomb(5,0))  
print("Pbinomial",Pbinomial(n, 0, p, q))  
  
print("Combinator",Pcomb(5,1))  
print("Pbinomial",Pbinomial(n, 1, p, q))  
  
print("Combinator",Pcomb(5,2))  
print("Pbinomial",Pbinomial(n, 2, p, q))  

print("P(<=2) ", Pbinomial(n, 0, p, q) + Pbinomial(n, 1, p, q) + Pbinomial(n, 2, p, q))  
