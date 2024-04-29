import numpy as np

class AlgebraLineal:
    def __init__(self, matriz):
        self.matriz = matriz

    def dot(self, otra):
        """Producto punto de dos matrices."""
        return np.dot(self.matriz, otra)

    def vdot(self, otra):
        """Producto punto de dos vectores aplanando antes si son matrices."""
        return np.vdot(self.matriz, otra)

    def solve(self, b):
        """Resuelve un sistema de ecuaciones lineales Ax = b para x."""
        return np.linalg.solve(self.matriz, b)

    def lstsq(self, b, rcond=None):
        """Resuelve la ecuación de mínimos cuadrados Ax = b."""
        return np.linalg.lstsq(self.matriz, b, rcond=rcond)[0]

    def roots(self):
        """Calcula las raíces de un polinomio con coeficientes dados en la matriz."""
        return np.roots(self.matriz)

    def polyval(self, x):
        """Evalúa un polinomio en x, donde los coeficientes del polinomio están en la matriz."""
        return np.polyval(self.matriz, x)

    def matrix_rank(self):
        """Devuelve el rango de la matriz."""
        return np.linalg.matrix_rank(self.matriz)

    def det(self):
        """Calcula el determinante de la matriz."""
        return np.linalg.det(self.matriz)

    def eig(self):
        """Calcula los valores y vectores propios de la matriz."""
        return np.linalg.eig(self.matriz)

    def inv(self):
        """Calcula la inversa de la matriz."""
        return np.linalg.inv(self.matriz)

    def norm(self, ord=None):
        """Calcula la norma de la matriz o vector."""
        return np.linalg.norm(self.matriz, ord=ord)