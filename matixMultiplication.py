import numpy
A = numpy.mat('0 0 0 0 6;2 0 0 0 0;2 0 0 0 0;2 3 3 0 0;0 3 3 6 0')
v = numpy.mat('6;6;6;6;6')
print(A*v)
print("#################")
for i in range(10000):
    z = A*v
    z = z/numpy.linalg.norm(z)
    #print (z)
    v = z
    #print("************") 
print (z)
'''
import numpy as np
A = np.mat('1 2; 3 4') # Matrix A with value a11=1, a12=2, a21=3, a22=4
v = np.mat('1; 1') # Vector v with values v11=1, v21=11
z = A*v
#np.linalg.norm(z) => sqrt(z11^2+ z21^2)
z = z/np.linalg.norm(z)
print (z)
'''
