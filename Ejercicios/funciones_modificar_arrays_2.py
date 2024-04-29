import numpy as np 

# np.concatenate

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.concatenate([a,b]))
c = np.concatenate([a,b])
print(c.shape)

print("\n")
a = np.array([[1,2,3]])
b = np.array([[4,5,6]])
print(np.concatenate([a,b]))
c = np.concatenate([a,b])
print(c.shape)


print("\n")
a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[7,8,9],
              [10,11,12]])
print(np.concatenate([a,b]))
c = np.concatenate([a,b])
print(c.shape)

# np.vstack 

print("\n")
c = np.vstack([a,b])
print(c)
print(c.shape)

# np.hstack

print("\n")
c = np.hstack([a,b])
print(c)
print(c.shape)

# np.split

d = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])

parte1, parte2 = np.split(d, [3])
print("\n")
print("Parte1:", parte1)
print("Parte2:", parte2)

parte1, parte2, parte3, parte4 = np.split(d, [3, 6, 9])
print("\n")
print("Parte1:", parte1)
print("Parte2:", parte2)
print("Parte3:", parte3)
print("Parte4:", parte4)

# np.column_stack
print("\n")
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack((a,b)))

# np.tile

a = np.array([1,2,3])
print(np.tile(a,4))

# np.repeat

a = np.array([1,2,3])
print(np.repeat(a,4))
