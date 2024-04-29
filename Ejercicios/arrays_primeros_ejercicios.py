import numpy as np 

array = np.array([1,2,3]) # Array unidimensional
array_2 = np.array((1,2,3)) # Array unidimensional
array_3 = np.array([[1,2,3],
                    [4,5,6]]) # Array bidimensional

print(array)
print(array_2)
print(array_3)

print("\nPrimer elemento de un array: ", array[0])
print("\Tercer elemento de un array: ", array_2[2])
print("Primera fila del array_3 y 2º elemento: ",array_3[0][1])
print("Primera fila del array_3 y 2º elemento: ",array_3[0,1])

# Tipo de dato
print("\n")
print("Tipo de variable para array_2: ", type(array_2))
print("Tipo de variable para array_3: ", type(array_3))

# Propiedades de los arrays (ndim, shape y size)
print("\n")
print("Dimensiones del array: ", np.ndim(array))
print("Dimensiones del array_3: ", np.ndim(array_3))

print("\n")
print("Forma del array: ", np.shape(array))
print("Forma del array_3: ", np.shape(array_3))

print("\n")
print("Numero de elementos del array: ", np.size(array))
print("Numero de elementos del array_3: ", np.size(array_3))