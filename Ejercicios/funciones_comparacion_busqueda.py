import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,4,3,2,1])

# np.less

array_less = np.less(a,b)
print(array_less)

# np.greater

print()
array_greater = np.greater(a,b)
print(array_greater)

# np.less_equal

print()
array_less_equal = np.less_equal(a,b)
print(array_less_equal)

# np.greater_equal

print()
array_greater_equal = np.greater_equal(a,b)
print(array_greater_equal)

# np.equal
print()
array_equal = np.equal(a,b)
print(array_equal)

# np.not_equal
print()
array_not_equal = np.not_equal(a,b)
print(array_not_equal)

# np.argmin
print()
indice_minimo = np.argmin(a)
print(indice_minimo)

# np.argmax
print()
indice_maximo = np.argmax(a)
print(indice_maximo)

#np.argsort

c = np.array([5,3,4,1])
print()
indices_ordenados = np.argsort(c)
print(indices_ordenados)

print()
indices_ordenados = np.argsort(-c)
print(indices_ordenados)

d = np.array([[5,3,4,1],
                 [2,3,4,5]]) 
print()
indices_ordenados = np.argsort(-d)
print(indices_ordenados)


# np.where
print()
c = np.array([5,3,4,1])
indices_where = np.where(c>=3)
print(indices_where)
print()
indices_seleccionados_where = c[indices_where]
print(indices_seleccionados_where)

# np.extract
print()
c = np.array([5,3,4,1])
condicion = c >= 4
indices_extraidos = np.extract(condicion, c)
print(indices_extraidos)
