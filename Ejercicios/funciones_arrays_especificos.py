import numpy as np

#np.arange

print(np.arange(0,10))
print(np.arange(0,11))
print(np.arange(0,11,2))
print(np.arange(11,0,-2))

#np.linspace

print(np.linspace(0,1,5))
print(np.linspace(0,1,9))

#np.identity

print(np.identity(3,dtype=int))

#np.eye

print(np.eye(3,dtype=int))
print(np.eye(3,5,dtype=int))
print(np.eye(3,5,1,dtype=int))
print(np.eye(3,5,2,dtype=int))

#np.diag

print(np.diag([1,3,5,4]))

#np.empty

print(np.empty((2,3)))

#np.tri

print(np.tri(3,3, k=0, dtype=int))
print(np.tri(4,4, k=0, dtype=int))
print(np.tri(3,4, k=0, dtype=int))