
# np.random.seed

# np.random.rand

# np.random.randint

# np.random.randn

# np.random.choice

# np.random.permutation

# np.random.shuffle

# np.pad

# np.transpose

# np.resize

#np.ravel

# np.concatenate

# np.vstack 

# np.hstack

# np.split

# np.column_stack

# np.tile

# np.repeat

# --------------------------------------------------------------------------------------------------------------------------

# Ejercicio 1

# Generar una imagen en escala de grises de 10 filas x 10 columnas 
# imágenes en escala de grises cada píxel es representado como un valor de intensidad entre 0 (negro) y 255 (blanco).
# Para ello generame un array con np.random.randint de size 10 x 10 donde los valores sean enteros, con valor mínimo 0 y máximo 255 
# los elementos del array tienen que ser dtype = np.uint8 ("unsigned integer 8 bits" -->  
#  tipo de datos se utiliza comúnmente para imágenes en escala de grises 
#  porque cada píxel puede ser representado como un valor de intensidad entre 0 (negro) y 255 (blanco).

import numpy as np
print()
imagen = np.random.randint(0, 256, size=(10, 10), dtype=np.uint8)
print(imagen)
print(imagen.shape)
print()

# Añade padding (np.pad) de 1 píxel con valor 0 (negro)

imagen_con_pad = np.pad(imagen, pad_width=1, mode='constant', constant_values=0)
print(imagen_con_pad)
print(imagen_con_pad.shape)
print()

# Utiliza np.ravel para aplanar la imagen y poder procesarla

imagen_aplanada = np.ravel(imagen_con_pad)

print("Imagen aplanada con padding:")
print(imagen_aplanada)
print(imagen_aplanada.shape)
print()

# --------------------------------------------------------------------------------------------------------------------------

# Ejercicio 2 

# Importa numpy 

# Establece una semilla aleatoria con np.random.seed.

# Crea un array llamado a de 1D con np.random.choice seleccionando 15 elementos de un rango de 1 a 50, con reemplazo.

# Redimensiona a a una forma de 5x3 usando np.resize.

# Utiliza np.random.shuffle para mezclar aleatoriamente las filas de a.

# Usa np.tile para repetir a 2 veces a lo largo de un nuevo eje, creando una matriz más grande.

# Aplica np.ravel para aplanar la matriz en un array 1D.

# --------------------------------------------------------------------------------------------------------------------------

# Importa numpy

import numpy as np

# # Crea la semilla

np.random.seed(42)

# # Crear un array 1D a seleccionando 15 elementos aleatorios entre 1 y 50

a = np.random.choice(range(1, 51), 15, replace=True)
print(a)
print("\n")

# # Redimensionar a a una forma de 5x3

a = np.resize(a, (5, 3))
print(a)
print("\n")


# # Mezclar aleatoriamente las filas de a

np.random.shuffle(a)
print(a)
print("\n")


# # Usar np.tile para repetir a 2 veces a lo largo de un nuevo eje

a_tile = np.tile(a, (2, 1))
print(a_tile)
print(a_tile.shape)
print("\n")


# # Aplanar la matriz en un array 1D

a_flat = np.ravel(a_tile)

print("Array final:")
print(a_flat)
print("\n")