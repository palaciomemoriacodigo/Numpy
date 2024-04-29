import numpy as np
from algebra_lineal import AlgebraLineal

matriz = np.array([[2, 1], 
                   [1, 2]])
b = np.array([1, 1])
algebra = AlgebraLineal(matriz)

print("Producto punto:", algebra.dot(b))
print("Solución de sistema lineal:", algebra.solve(b))
print("Rango de la matriz:", algebra.matrix_rank())
print("Determinante:", algebra.det().round(1))
print("Inversa de la matriz:")
print(algebra.inv())
print("Norma de la matriz:", algebra.norm())

coeficientes_polinomio = np.array([1, -3, 2])  
algebra_polinomio = AlgebraLineal(coeficientes_polinomio)
raices = algebra_polinomio.roots()
print("Raíces del polinomio:", raices)

x_eval = np.linspace(0, 3, 10) 
print("Evaluación del polinomio en puntos:")
print(algebra_polinomio.polyval(x_eval))

vector = np.array([3, 4])
algebra_vector = AlgebraLineal(vector)
print("Norma del vector:", algebra_vector.norm())