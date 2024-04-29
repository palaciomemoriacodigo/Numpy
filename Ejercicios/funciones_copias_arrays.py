import numpy as np 

array_base = np.array([[1,2,3],
                       [4,5,6]])
print(array_base)
print(array_base.shape)
print(array_base.ndim)
print(type(array_base))

#np.zeros_like

print("\n")
print(np.zeros_like(array_base))

#np.ones_like

print("\n")
print(np.ones_like(array_base)*14)


#np.full_like

print("\n")
print(np.full_like(array_base,14))

# np.copy

print("\n")
array_copia_base = np.copy(array_base)

array_copia_base[0][2] = 800

print("\n")
print(array_copia_base)

print("\n")
print(array_base)