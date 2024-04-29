import numpy as np
import timeit

elementos = 100000

# array de NumPy y una lista con los mismos elementos
numpy_array = np.arange(elementos)
python_lista = list(range(elementos))

# print(numpy_array)
# print(python_lista)


# print(type(numpy_array))
# print(type(python_lista))

# Definir la función que suma todos los elementos para NumPy
def suma_array():
    return np.sum(numpy_array)

# Definir la función que suma todos los elementos para la lista de Python
def suma_lista():
    return sum(python_lista)

# Medir el tiempo de ejecución
tiempo_array = timeit.timeit(suma_array, number=100)
tiempo_lista = timeit.timeit(suma_lista, number=100)

print(f"Tiempo de ejecución usando NumPy: {tiempo_array} segundos")
print(f"Tiempo de ejecución usando lista de Python: {tiempo_lista} segundos")