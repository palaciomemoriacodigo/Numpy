import numpy as np

# np.char.add

nombres = np.array(['Pedro','Juan'])
apellidos = np.array(['Pérez López','López Pérez'])
apellidos_con_espacio = np.char.add(" ", apellidos)
print(apellidos_con_espacio)
nombres_completo = np.char.add(nombres,apellidos_con_espacio)
print(nombres_completo)

url = np.array(['palaciomemoriacodigo.com/user/',
                'palaciomemoriacodigo.com/admin/',
                'palaciomemoriacodigo.com/api/'])
salida = np.array(['profile','dashboard','home'])
url_completa = np.char.add(url,salida)
print()
print(url_completa)

nombres = np.array(['Pedro','Juan'])
mensaje = ' se ha registrado correctamente'
print()
mensaje_completo = np.char.add(nombres,mensaje)
print(mensaje_completo)

# np.char.rjust

numeros = np.array(["1", "10", "100", "1000"])
numeros_alineados = np.char.rjust(numeros, 4)
print()
print(numeros_alineados)

# np.char.split

frases = np.array(["hola mundo", "curso, a,b,c, de numpy", "palaciomemoriacodigo"])
palabras = np.char.split(frases, ",")
print()
print(palabras)
print(palabras[0])
print(palabras[1])
print(palabras[2])


nombres = np.array(['Pedro','Juan'])
apellidos = np.array(['Pérez López','López Pérez'])
apellidos_con_espacio = np.char.add(" ", apellidos)
print(apellidos_con_espacio)
nombres_completo = np.char.add(nombres,apellidos_con_espacio)
print(nombres_completo)
nombres_separados = np.char.split(nombres_completo, " ")
print(nombres_separados)
print(nombres_separados[0])
print(nombres_separados[1])

# np.char.replace

ciudades = np.array(["madrid", 'barcelona', 'murcia', 'Madrid', 'andalucia'])

texto_modificado = np.char.replace(ciudades, "madrid", "Madrid")
texto_modificado = np.char.replace(texto_modificado, "barcelona", "Barcelona")
texto_modificado = np.char.replace(texto_modificado, "murcia", "Murcia")
texto_modificado = np.char.replace(texto_modificado, "andalucia", "Andalucia")
print()
print(texto_modificado)

# np.char.strip

usuarios = np.array(["  palaciomemoriacodigo", "   @gmail.com"])
usuarios_limpio = np.char.strip(usuarios)
print()
print(usuarios_limpio)

# np.char.count

texto = np.array(['pera manzana pera', "gallina pera pomelo", "perro gallina platano"])
conteo_texto_pera = np.char.count(texto, 'pera')
print()
print(conteo_texto_pera)

# np.char.startwith

url = np.array(["http://palaciomemoriacodigo.com",
                "https://palaciomemoriacodigo.com",
                "ftp://palaciomemoriacodigo.com"])

url_validas = np.char.startswith(url, "https")
print()
print(url_validas)

telefonos = np.array(["685123456", 
                      "34632456789",
                      "351234567898"])

telefonos_validos = np.char.startswith(telefonos, "34")
print()
print(telefonos_validos)

telefonos_nuevos = []
for telefono in telefonos:
    if np.char.startswith(telefono,"34") and len(telefono) == 11:
        telefonos_nuevos.append(telefono)
    elif len(telefono) == 9:
        telefonos_nuevos.append(np.char.add('34',telefono))
    else:
        telefonos_nuevos.append(None)
        
print()
print(telefonos_nuevos[0])
print(telefonos_nuevos[1])
print(telefonos_nuevos[2])

# np.char.endswith

archivos = np.array(["caja.png", "perro.jpeg", "documento.pdf"])
archivos_pdf = np.char.endswith(archivos, ".pdf")
print()
print(archivos[archivos_pdf])

email = np.array(['palaciomemoriacodigo@gmail.com','palaciomemoriacodigo@hotmail.com','palaciomemoriacodigo@gmal.com'])
email_validos = np.char.endswith(email, "gmail.com") + np.char.endswith(email, "hotmail.com")
print()
print(email[email_validos])


# np.char.upper

nombres = np.array(['Juan', 'pedro'])
nombres_mayusculas = np.char.upper(nombres)
print()
print(nombres_mayusculas)

# np.char.lower

nombres = np.array(['Juan', 'pedro'])
nombres_minusculas = np.char.lower(nombres)
print()
print(nombres_minusculas)

# np.char.capitalize

nombres = np.array(['Juan', 'pedro'])
nombres_minusculas = np.char.lower(nombres)
print()
print(nombres_minusculas)


ciudades = np.array(["madrid", 'barcelona', 'murcia', 'Madrid', 'andalucia'])
ciudades_capitalize = np.char.capitalize(ciudades)
print()
print(ciudades_capitalize)
