# from generador_arrays import *
import numpy as np
from generador_arrays import GeneradorArrays

print("\n")
array_de_ceros = GeneradorArrays.zeros((3, 4))
print(array_de_ceros)
print("\n")

print(type(array_de_ceros))
array_de_unos = GeneradorArrays.ones((2, 2))
print(array_de_unos)
print("\n")

array_full = GeneradorArrays.full((2, 3), fill_value=5, dtype=int)
print(array_full)
print("\n")

array_arange = GeneradorArrays.arange(0, 10, 2)
print(array_arange)
print("\n")

array_cortado = GeneradorArrays.linspace(0, 1, 5)
print(array_cortado)
print("\n")

array_eye = GeneradorArrays.eye(3,4,dtype=int)
print(array_eye)
print("\n")

array_diag = GeneradorArrays.diag([1, 2, 3, 4],dtype=int)
print(array_diag)
print("\n")

array_id = GeneradorArrays.identity(3,dtype=int)
print(array_id)
print("\n")

array_empty = GeneradorArrays.empty((2, 3))
print(array_empty)
print("\n")

array_tri = GeneradorArrays.tri(3,dtype=int)
print(array_tri)
print("\n")

array_original = np.array([[1, 2, 3], 
                           [4, 5, 6]], dtype=int)

zeros_like_array = GeneradorArrays.zeros_like(array_original)
print(zeros_like_array)
print("\n")

ones_like_array = GeneradorArrays.ones_like(array_original)
print(ones_like_array)
print("\n")

full_like_array = GeneradorArrays.full_like(array_original, fill_value=9)
print(full_like_array)
print("\n")

copy_of_array = GeneradorArrays.copy(array_original)
copy_of_array[0][0] = 400
print(copy_of_array)
print("\n")

array_rand = GeneradorArrays.random_rand(3, 2)
print(array_rand)
print("\n")

array_randint = GeneradorArrays.random_randint(1, 10, (3, 3))
print(array_randint)
print("\n")

array_randn = GeneradorArrays.random_randn(3, 3)
print(array_randn)
print("\n")

array_choice = GeneradorArrays.random_choice([1, 2, 3, 4, 5], size=10)
print(array_choice)
print("\n")

array_permutation = GeneradorArrays.random_permutation(10)
print(array_permutation)
print("\n")

array_original = np.array([1, 2, 3, 4, 5])
print(array_original)
print("\n")

array_shuffle = GeneradorArrays.random_shuffle(array_original.copy())
print(array_shuffle)