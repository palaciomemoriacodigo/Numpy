import numpy as np

array_1 = np.array([1,2,3,4])
array_2 = np.array([5,6,7,8])

# np.save

np.save("Ejercicios/array1.npy", arr = array_1)

# np.savez

# (file, **kwargs)
np.savez("Ejercicios/arrays.npz", arr1 = array_1, arr2 = array_2)

# np.load

array1_cargado = np.load("Ejercicios/array1.npy")
print()
print(array1_cargado)


arrays_cargado = np.load("Ejercicios/arrays.npz")
arrays_cargado_1 = arrays_cargado['arr1']
arrays_cargado_2 = arrays_cargado['arr2']
print()
print(arrays_cargado_1)
print(arrays_cargado_2)

# np.savetxt

np.savetxt('Ejercicios/array_text.txt', array_1, delimiter=',')

np.savetxt('Ejercicios/array_text_2.txt', [array_1,array_2], delimiter=',')

# np.loadtxt

carga_array_txt_1 = np.loadtxt("Ejercicios/array_text.txt", delimiter= ",")
print()
print(carga_array_txt_1)

carga_array_txt_2 = np.loadtxt("Ejercicios/array_text_2.txt", delimiter= ",")
print()
print(carga_array_txt_2)