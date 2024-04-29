import numpy as np

array = np.array([1,2,3])
array_2 = np.array([4,5,6])

print(array + array_2)
print(np.add(array,array_2))

print("\n")

print(array - array_2)
print(np.subtract(array,array_2))

print("\n")

print(array * array_2)
print(np.multiply(array,array_2))

print("\n")

print(array / array_2)
print(np.divide(array,array_2))

print("\n")
print(array)
print(np.power(array, 2))
print(np.power(array, 3))

print("\n")
cociente, resto = np.divmod(array_2,array)
print(cociente)
print(resto)

print("\n")
array_vabs = np.array([-1,-2,3,4])
print(np.abs(array_vabs))

print("\n")
print(np.e)
print(np.pi)

angulo = np.pi/4
seno = np.sin(angulo)
print(seno)
cos = np.cos(angulo)
print(cos)
tan = np.tan(angulo)
print(tan)
arcseno = np.arcsin(angulo)
print(arcseno)
arccos = np.arccos(angulo)
print(arccos)
arctg = np.arctan(angulo)
print(arctg)

raiz = np.sqrt(4)
print(raiz)

raiz_cuarta = np.power(4**4, 1/4)
print(raiz_cuarta)

exponencial = np.exp(1)
print(exponencial)
print(np.e)


exponencial = np.exp(2)
print(exponencial)
print(np.e*np.e)

log_neperiano = np.log(np.e)
print(log_neperiano)

log_base_10 = np.log10(0.1)
print(log_base_10)

print(seno)
print(np.round(seno,3))

print(np.e)
print(np.trunc(np.e))