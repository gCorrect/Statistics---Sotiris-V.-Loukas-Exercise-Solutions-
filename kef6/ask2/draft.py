# https://www.geeksforgeeks.org/numpy-ndarray-view-in-python/

# Python program explaining 
# numpy.ndarray.view() function
 
import numpy as geek
 
a = geek.arange(10, dtype ='int16')

print("a is: \n", a)

# a += 1 
# print("a  += 1 = ", a)

# using view() method
v = a.view('int32')
print("\n After using view() with dtype = 'int32' a is : \n", a)
 
v += 1
 
# addition of 1 to each element of v
print("\n After using view() with dtype = 'int32' and adding 1 a is : \n", a)

a += 1 
print("a  += 1 = ", a)
# ------------------------------------------
print("-------------------------------------\n")

a = geek.arange(10, dtype ='int16')
print("a is:", a)
 
# Using view() method
v = a.view('int16')
print("\n After using view() with dtype = 'int16' a is :\n", a)
 
v += 1
# addition of 1 to each element of v
print("\n After using view() with dtype = 'int16' and adding 1 a is : \n", a)

# ------------------------------------------
print("-------------------------------------\n")

a = geek.arange(10, dtype ='int16')
print("a is: \n", a)
 
v = a.view('int8')
print("\n After using view() with dtype = 'int8' a is : \n", a)
 
v += 1
# addition of 1 to each element of v
print("\n After using view() with dtype = 'int8' and adding 1 a is : \n", a)
