import numpy as np
from numpy_io import NumpyIO

array = np.array([1, 2, 3, 4, 5])
NumpyIO.save("Ejercicios/salida_npy.npy", array)
loaded_array = NumpyIO.load("Ejercicios/salida_npy.npy")
print("Array cargado:", loaded_array)

NumpyIO.savetxt("Ejercicios/salida_txt.txt", array, fmt='%d')
loaded_array_txt = NumpyIO.loadtxt("Ejercicios/salida_txt.txt")
print("Array cargado desde texto:", loaded_array_txt)