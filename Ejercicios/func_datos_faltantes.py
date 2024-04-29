import numpy as np 

array = np.array([[14,6, np.nan],
                  [-np.inf, 8, np.inf]])

# np.isnan

print()
print(np.isnan(array))

# np.isinf

print()
print(np.isinf(array))

# np.isfinite

print()
print(np.isfinite(array))

# np.nan_to_num
print()
limpiar_array = np.nan_to_num(array, nan=0, posinf=100, neginf=-1).round(2).astype(int)
print(limpiar_array)

print()
print(np.isnan(limpiar_array))
print(np.isinf(limpiar_array))
print(np.isfinite(limpiar_array))

array_dos = np.array([[1, 2, np.nan],
                      [3,4,5]])

# np.nanmean, np.nanvar, np.nanstd

print(np.nanmean(array_dos))
print(np.nanvar(array_dos))
print(np.nanstd(array_dos))

array_tres = np.array([[1,2, np.nan],
                       [-np.inf,3,np.inf],
                      [4,5,np.nan]])
print()
array_mappeado = np.nan_to_num(array_tres, nan= np.nan, posinf = np.nan, neginf = np.nan)
print(array_mappeado)

print(np.nanmean(array_mappeado))
print(np.nanvar(array_mappeado))
print(np.nanstd(array_mappeado))

print()
array_finito = np.isfinite(array_tres)
print(array_finito)
print()
print(np.nanmean(array_tres[array_finito]))
print(np.nanvar(array_tres[array_finito]))
print(np.nanstd(array_tres[array_finito]))


# np.allclose y np.isclose

array_tres = np.array([1,2,3,4])
array_cuatro = np.array([1,2,3.05,4])

print()
print(np.allclose(array_tres,array_cuatro, atol= 0.03))
print(np.isclose(array_tres,array_cuatro, atol= 0.1))

# np.interp

x = np.array([0,1,3,4])
y = np.array([0,1,8,16])
x_new = np.array([2])

y_new = np.interp(x_new, x, y)
print(y_new)


