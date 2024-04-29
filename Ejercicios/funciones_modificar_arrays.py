import numpy as np

# np.pad

array = np.array([1,2,3])
print(np.pad(array,(1,1), constant_values = (7,5)))

print("\n")
array_2 = np.zeros(shape=(2,2), dtype=int)
print(np.pad(array_2, pad_width=2, mode='constant', constant_values=8))

# np.transpose

c = np.array([[1,2],
             [3,4]])
print("\n")
print(c)
print(np.transpose(c))
print(np.transpose(np.transpose(c)))

# np.reshape
print("\n")
array_tres = np.array([1,2,3,4,5,6])
print(np.reshape(array_tres, (2,3)))
print(np.reshape(array_tres, (3,2)))
print(np.reshape(array_tres, (6,1)))

# Supongamos que tienes un conjunto de datos de imágenes con 1000 imágenes de 28x28 píxeles
# y deseas redimensionar cada imagen a un vector de 1D de tamaño 784 

#datos_imagenes = np.random.random((1000, 28, 28))  
#datos_redimensionados = np.reshape(datos_imagenes, (1000, 28*28))  
#print(datos_redimensionados)




datos = np.random.random((1000, 5))
print(datos)

# variables independientes
X = datos[:, :-1]

# variable dependiente
y = datos[:, -1]

print(y[0:3])
# vector columna para una regresión
y = np.reshape(y, (-1, 1))
print(y[0:3])

#np.resize

array_cuatro = np.array([1,2,3])
print("\n")
print(np.resize(array_cuatro, (2,3)))
print(np.resize(array_cuatro, (4,6)))
print(np.resize(array_cuatro, (4,7)))

#np.ravel
print("\n")
array_ravel = np.array([[1,2,3],
                        [4,5,6]])
print(array_ravel)
print(np.ravel(array_ravel))

array_ravel = np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]])
print(array_ravel)
print(np.ravel(array_ravel))