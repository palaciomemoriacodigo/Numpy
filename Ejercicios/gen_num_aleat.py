import numpy as np

# np.random.seed

# np.random.seed(42)

# np.random.rand

print(np.random.rand(3,2))

# Entre 1 y 4 (Amplitud 4 - 1 = 3 y el limite inferior = 1)

print(np.random.rand(3,2) * 3 + 1)

# Entre -3 y 4 (Amplitud 4 - (-3) = 7 y el limite inferior = -3)

print(np.random.rand(3,2) * 7 -3)

# np.random.randint

print(np.random.randint(-4,5,size=(3,2)))

# np.random.randn

# np.random.seed(42)
print(np.random.randn(5))


# np.random.seed(42)
print(np.random.randn(2,3))

#np.random.seed(42)
media = 0
sigma = np.sqrt(1)
numeros = media + sigma * np.random.randn(2,3)
print(numeros)


# np.random.seed(42)
media = 4
sigma = np.sqrt(2)
numeros = media + sigma * np.random.randn(2,3)
print(numeros)

# np.random.choice
print("\n")
print(np.random.choice(['platano','gato','perro'], size = 10, replace=True))

print(np.random.choice(['platano','gato','perro'], size = 2, replace=False))

print(np.random.choice(['platano','gato',3], size = 2, replace=False))

print(np.random.choice([1,2,3], size = 2, replace=False))

# np.random.permutation

# np.random.seed(42)
print(np.random.permutation([1,2,2,3,4,5]))

print("\n")
np.random.seed(42)
array = np.array([1,2,2,3,4,5])
print(np.random.permutation(array))
print(array)
np.random.seed(42)
array = np.random.permutation(array)
print(array)

# np.random.shuffle
print("\n")
array = np.array([1,2,2,3,4,5])
print(array)
np.random.shuffle(array)
print(array)