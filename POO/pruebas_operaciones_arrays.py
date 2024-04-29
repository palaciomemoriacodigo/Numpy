import numpy as np
from operaciones_arrays import OperacionesArrays

array = np.array([[1, 2, 3], [4, 5, 6]])
operaciones = OperacionesArrays(array)

array_pad = operaciones.pad(pad_width=1, constant_values=0)
print("\n")
print("Padded Array:\n", array_pad)

array_transpose = operaciones.transpose()
print("\n")
print("Transposed Array:\n", array_transpose)

array_reshape = operaciones.reshape((6,))
print("\n")
print("Reshaped Array:\n", array_reshape)

array_resize = operaciones.resize((3, 4))
print("\n")
print("Resized Array:\n", array_resize)

array_ravel = operaciones.ravel()
print("\n")
print("Raveled Array:\n", array_ravel)



array_original = np.array([[1, 2], [3, 4]])
operaciones = OperacionesArrays(array_original)
segundo_array = [np.array([[5, 6], [7, 8]])]


concatenated = operaciones.concatenate(segundo_array)
print("Concatenated:\n", concatenated)

vstacked = operaciones.vstack(segundo_array)
print("VStacked:\n", vstacked)

hstacked = operaciones.hstack(segundo_array)
print("HStacked:\n", hstacked)

splitted = operaciones.split(2)
print("Splitted:\n", splitted)

column_stacked = operaciones.column_stack(segundo_array)
print("Column Stacked:\n", column_stacked)

tiled = operaciones.tile((2, 2))
print("Tiled:\n", tiled)

repeated = operaciones.repeat(2)
print("Repeated:\n", repeated)



array_op = np.array([1, 2, 3, 4, 5])
operaciones = OperacionesArrays(array_op)

print("\nSuma:", operaciones.sum())
print("\nProducto:", operaciones.prod())
print("\nMedia:", operaciones.mean())
print("\nDesviación estándar:", operaciones.std())
print("\nVarianza:", operaciones.var())
print("\nMediana:", operaciones.median())
print("\nPercentil 90:", operaciones.percentile(90))
print("\nCuantil 0.5:", operaciones.quantile(0.5))
print("\nMínimo:", operaciones.min())
print("\nMáximo:", operaciones.max())
print("\nSuma acumulativa:", operaciones.cumsum())
print("\nProducto acumulativo:", operaciones.cumprod())
print("\nCoeficiente de correlación:", operaciones.corrcoef())
print("\nAlgún elemento es True:", operaciones.any())
print("\nTodos los elementos son True:", operaciones.all())
print('\n')

array = np.array([1, 2, 3, 4, 5])
operaciones = OperacionesArrays(array)
print("Menor que 3:", operaciones.less(3))
print("Menor o igual que 3:", operaciones.less_equal(3))
print("Mayor que 3:", operaciones.greater(3))
print("Mayor o igual que 3:", operaciones.greater_equal(3))
print("Igual a 3:", operaciones.equal(3))
print("No igual a 3:", operaciones.not_equal(3))
print("Índice del elemento mínimo:", operaciones.argmin())
print("Índice del elemento máximo:", operaciones.argmax())
print("Índices para ordenar el array:", operaciones.argsort())
print("Elementos donde > 4 (5 si sí, 0 si no):", operaciones.where(array > 4, 5, 0))
print("Extraer elementos > 3:", operaciones.extract(array > 3))



array = np.array([1, 2, np.nan, 4, 5])
array2 = np.array([1, 2.1, np.nan, 3.9, 5])
operaciones = OperacionesArrays(array)
operaciones2 = OperacionesArrays(array2)

print("¿Contiene NaN?:", operaciones.isnan())
print("¿Contiene Infinitos?:", operaciones.isinf())
print("¿Es Finito?:", operaciones.isfinite())
print("NaN convertido a Número:", operaciones.nan_to_num())
print("Media ignorando NaN:", operaciones.nanmean())
print("Varianza ignorando NaN:", operaciones.nanvar())
print("Desviación Estándar ignorando NaN:", operaciones.nanstd())
print("Todos cercanos entre sí:", operaciones.allclose(array2, atol=0.3))  
print("Cercanía elemento a elemento:", operaciones.isclose(array2, atol=0.3))

x = [1, 2, 3]
y = [3, 2, 0]

x2 = np.array([1, 1.5, 2.5, 3])
print("Valores interpolados:", operaciones.interp(x, y, x2))