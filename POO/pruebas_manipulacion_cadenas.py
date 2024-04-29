import numpy as np
from manipulacion_cadenas import ManipulacionCadenas
texto = np.array(["bienvenidos a palaciomemoriacodigo", "estoy recorriendo las diferentes posibilidades que ofrece Numpy", "¡¡¡No os lo perdais!!!"])
manipulador = ManipulacionCadenas(texto)

print("Añadir '!!!':", manipulador.add("!!!"))
print()
print("Justificar a la derecha:", manipulador.rjust(20, '-'))
print()
print("Relleno con ceros:", manipulador.zfill(15))
print()
print("Dividir cadenas:", manipulador.split())
print()
print("Reemplazar 'estoy' por 'estamos':", manipulador.replace("estoy", "estamos"))
print()
print("Tira espacios:", manipulador.strip())
print()
print("Contar 'o':", manipulador.count('o'))
print()
print("Empieza con 'bienvenidos':", manipulador.startswith('bienvenidos'))
print()
print("Termina con 'codigo':", manipulador.endswith('codigo'))
print()
print("Convertir a mayúsculas:", manipulador.upper())
print()
print("Convertir a minúsculas:", manipulador.lower())
print()
print("Capitalizar:", manipulador.capitalize())