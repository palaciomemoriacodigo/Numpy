import numpy as np

# np.sum

print()
a = np.array([1,2,3,4,5])
print(np.sum(a))

# np.prod
print()
print(np.prod(a))

# np.mean

print()
print(np.mean(a))

# np.var y np.std
print()
print(np.var(a))
print()
print(np.std(a))

print()
var = ((1-3)**2 + (2-3)**2 + (3-3)**2 + (4-3)**2 + (5-3)**2 )/5
print(var)

print()
std = np.sqrt(var)
print(std)

# np.median 

print()
b = np.array([1,2,3,7,20,50])
print(np.median(b))

# np.percentile y np.quantile
print()
a = np.array([1,2,3,4,5,6,7,8,9])
print(np.percentile(a,25))
print(np.quantile(a,0.25))


import pandas as pd

df = pd.DataFrame(a, columns = ['Numeros'])

print(df)

print(df.info())

print(df.describe())


# np.min y np.max
 
print()
print(np.min(a))
print(np.max(a))

# np.cumsum y np.cumprod

a = np.array([1,2,3,4,5])
print()
print(np.cumsum(a))
print(np.cumprod(a))

# np.corrcoef 
print()
a = np.array([1,2,3,4,5])
b = np.array([2,4,6,8,10])
print(np.corrcoef(a,b))

print()
a = np.array([1,2,3,4,5])
b = np.array([2,4,6,8,40])
print(np.corrcoef(a,b))


print()
a = np.array([1,2,3,4,5])
b = np.array([2,4,6,8,40])
c = np.array([-200,-300,-800,-1220,-3000])

matriz = np.array([a,b,c])
print(matriz.shape)

matriz_corr = np.corrcoef(matriz)
print(matriz_corr)

# np.any 

a = np.array([7,20,8,9,5])
print()
array_any = np.any(a > 2)
print(array_any)

# np.all

print()
array_all = np.all(a > 2)
print(array_all)