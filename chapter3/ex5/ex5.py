import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'libraries'))
from functions import *  
 
Psum4= P(3,36)
Psum9= P(4,36)
Psum3=P(2,36)
Psum6=P(5,36)

print("Psum4", Psum4)
print("Psum9", Psum9)
print("PNotsum3", 1 - Psum3)
print("PNotsum6", 1 - Psum6)


