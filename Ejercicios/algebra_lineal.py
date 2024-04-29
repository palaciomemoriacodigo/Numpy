import numpy as np

# np.dot

a = np.array([1,2])
b = np.array([3,4])

print()
print(np.dot(a,b))

# a*b = a1*b1 + a2*b2 = 1*3 + 2*4 = 11

a = np.array([[1,2],
              [3,4]])

b = np.array([[2,0],
              [1,2]])

print()
print(np.dot(a,b))

# 1*2 + 2*1 = 4
# 1*0 + 2*2 = 4
# 3*2 + 4*1 = 10
# 3*0 + 4*2 = 8

# np.vdot

a = np.array([1+2j, 1+2j])
b = np.array([1+3j, 1+2j])

# i = sqrt(-1) --> i**2 --> -1
print()
print(np.vdot(a,b))
# (1-2j)(1+3j) + (1-2j)(1+2j) = (1+3j-2j -6j**2) + (1+2j-2j -4j**2) = (1j + 7) + (5) = 12 + 1j

# np.linalg.solve 

a = np.array([[3,1], 
              [1,2]])
b = np.array([9,8])
solucion = np.linalg.solve(a,b).astype(int)
print()
print(solucion)

# 3x + y = 9
# x + 2y = 8

# np.linalg.lstsq

a = np.array([[1,1],
              [1,2],
              [1,3]])

b = np.array([6,5,7])

x, residuos, rango, s = np.linalg.lstsq(a,b,rcond=None)

print()

# x + y = 6 (5 + 0.5 = 5.5 / diferencia 0.5)
# x + 2y = 5 (5 + 2*0.5 = 6 / diferencia 1)
# x + 3y = 7 (5 + 3*0.5 = 6.5 / diferencia 0.5)

print(x)

print()

print((0.5)**2 + (1)**2 + (0.5)**2)
print(residuos)

print()
print(rango)

# np.roots

ec = np.array([1,-4, 3]) # x**2 -4x +3
raices = np.roots(ec)
print()
print(raices)

# (-b +- sqrt(b**2 -4*ac))/2a = (4 +- sqrt(16-12))/2 = (4 +-2)/2 = 3,1

# np.polyval

array = np.array([1,0,-4]) # x**2 +0x -4 = x**2 -4
array_2 = np.array([2,0,-2])
valores = np.polyval(array,array_2)
print()
print(valores)

# np.linalg.matrix_rank

matriz = np.array([[1,2],
                   [2,4]])

rango = np.linalg.matrix_rank(matriz)
print()
print(rango)

matriz = np.array([[1,2],
                   [3,4]])

rango = np.linalg.matrix_rank(matriz)
print()
print(rango)


matriz = np.identity(3)
print(matriz)
rango = np.linalg.matrix_rank(matriz)
print()
print(rango)

# np.linalg.det

a = np.array([[1,2],
             [3,4]])

determinante = np.linalg.det(a).astype(int)
print()
print(determinante)

# 1*4 - (3*2) = -2

a = np.array([[1, 2, 1],
              [1, 2, 2],
              [2, 3, 2]])

determinante = np.linalg.det(a).astype(int)
print()
print(determinante)

# (1*2*2) + (2*2*2) + (1*1*3) - ((1*2*2) + (2*1*2) + (1*2*3)) = 4 + 8 + 3 -4 -4 -6 = 1

# np.linalg.eig 

a = np.array([[1, 1],
              [2,2]])

autovalores, autovectores = np.linalg.eig(a)
print()
print(autovalores)
print()
print(autovectores)

#(1 -lambda 1)
#(2 2 - lambda)

# Determinante

# (1 -lambda)(2 - lambda) - (2*1) = 2 -lambda -2lambda +lambda**2 -2 = -3lambda + lambda **2 = lambda(-3 + lambda) = 0 // 0,3

# lambda = 0

#(1  1) --> x + y = 0 --> x = -y --> [1,-1]T
#(2 2)


# lambda = 3

#(-2 1) --> -2x + y --> y = 2x --> [1,2]T
#(2 -1)


# np.linalg.inv

a = np.array([[1,2,2],
              [3,2,4],
              [2,1,3]])

inv = np.linalg.inv(a)
print()
print(inv)

print(np.linalg.det(a))

# a^-1 = 1/det(a) * adj(a)

# (-1)**i+j * det(aij)


# np.linalg.norm 

array = np.array([1,2,3])
distancia = np.linalg.norm(array)
print()
print(distancia)

print(np.sqrt((1**2) + (2**2) + (3**2)))

