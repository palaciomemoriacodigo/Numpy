# array = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# zeros_array = np.zeros((3, 4),dtype=int)

# ones_array = np.ones((2, 3),dtype=int)

# full_array = np.full((2, 2),fill_value=7,dtype=int)

# arange_array = np.arange(0, 10, 2)

# np.linspace(0, 1, 5)

# np.identity(3,dtype=int)

# np.eye(3,dtype=int)

# np.diag([1, 2, 3, 4],dtype=int)

# array_empty = np.empty((2, 3))

# array_tri = np.tri(3,dtype=int)

# array_zeros_like = np.zeros_like(array)

# array_ones_like = np.ones_like(array)

# array_full_like = np.full_like(array)

# array_copy = np.copy(array)


#-----------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 1 

# Generar un conjunto de puntos para usar en una gráfica (matplotlib o seaborn) o para muestreo.

# APARTADO 1

# Generar 10 puntos entre 1 y 10

import numpy as np
puntos = np.arange(1,11,1)
print(puntos)

# Generar 10 puntos linealmente espaciados entre 0 y 1 

print("\n")
puntos_linealmente_espaciados = np.linspace(0, 1, 10)
print(puntos_linealmente_espaciados)

#-----------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 2


# importa la libreria de numpy y como alias np

# Crea un array con 3 filas y 3 columnas (con valores del 1 al 9) y guardalo como array_original 

# Crea 3 arrays nuevos, realizando copias del array_original, en el primero de ellos con la misma forma y dimensiones, pero con ceros,
# en la segundo con unos y en el tercero donde todos los elementos sean cuatros.

# Crea un array que que sea la suma del array_original y el array almacenado con unos.

# Crea un array que que sea la resta del array_original y el array almacenado con cuatros

# Crea un array que sea la multiplicacion del array con unos y el array con cuatros.

# Imprime por pantalla los 3 ultimos arrays que te he solicitado (correspondiente suma, resta, multiplicacion)

import numpy as np

array_original = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

zeros_like_array = np.zeros_like(array_original)
ones_like_array = np.ones_like(array_original)
full_like_array = np.full_like(array_original, 4)


array_suma = array_original + ones_like_array
array_resta = array_original - full_like_array
array_multiplicacion = ones_like_array * full_like_array


print("Array correspondiente a la suma:\n", array_suma)
print("Array correspondiente a la resta:\n", array_resta)
print("Array correspondiente a la multiplicacion:\n", array_multiplicacion)
#-----------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 3

# Creame un array que corresponda a una matriz identidad de 5x5 (cuadrada)

# Posteriormente creame un array que corresponda a una matriz identidad de 5x5 (cuadrada) modificada donde la diagonal principal 
# (de la esquina superior izquierda a la inferior derecha) se desplace una posición hacia la derecha.

# Los elementos de ambas matrices deben ser enteros.

print("\n")
print(np.identity(5,dtype=int))

print("\n")
import numpy as np
print(np.eye(N=5,k=1,dtype=int))

#-----------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 4

# Creame el siguiente array:

# array([[1, 1, 1, 1],
#        [2, 2, 2, 2],
#        [3, 3, 3, 3],
#        [4, 4, 4, 4]])

# sin utilizar                     array = np.array([[1,1,1,1],
#                                                   [2,2,2,2],
#                                                   [3,3,3,3
#                                                   [4,4,4,4]]])
# print(array)

print("\n")
array_base_1 = np.ones((4, 4),dtype=int)
array_base_1[0][0] = 1
array_base_1[0][1] = 1
array_base_1[0][2] = 1
array_base_1[0][3] = 1

array_base_1[1][0] = 2
array_base_1[1][1] = 2
array_base_1[1][2] = 2
array_base_1[1][3] = 2

array_base_1[2][0] = 3
array_base_1[2][1] = 7
array_base_1[2][2] = 3
array_base_1[2][3] = 3

array_base_1[3][0] = 4
array_base_1[3][1] = 4
array_base_1[3][2] = 4
array_base_1[3][3] = 4

print(array_base_1)

print("\n")
array_base_2 = np.ones((4, 4),dtype=int)
array_base_2[0] = array_base_2[0] * 1
array_base_2[1] = array_base_2[1] * 2
array_base_2[2] = array_base_2[2] * 3
array_base_2[3] = array_base_2[3] * 4
print(array_base_2)


print("\n")
array_base_3 = np.ones((4, 4),dtype=int)
array_base_3[0] *= 1
array_base_3[1] *= 2
array_base_3[2] *= 3
array_base_3[3] *= 4
print(array_base_3)


print("\n")
for i in range(1,5):
    print(i)
    
base_array = np.zeros((4,4),dtype=int)
print(base_array)
print("\n")

for i in range(1, 5):  
    base_array[i-1] = i
    print(i)

print("\n")
print(base_array)


base_array[2][1] = 7
print(base_array)