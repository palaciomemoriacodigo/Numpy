import numpy as np

class ManipulacionCadenas:
    def __init__(self, array):
        self.array = array

    def add(self, otro):
        """Concatena elementos de dos arrays de cadenas."""
        return np.char.add(self.array, otro)

    def rjust(self, width, fillchar=' '):
        """Justifica a la derecha los strings en el array usando fillchar."""
        return np.char.rjust(self.array, width, fillchar)

    def zfill(self, width):
        """Rellena las cadenas del array con ceros a la izquierda hasta alcanzar la longitud especificada."""
        return np.char.zfill(self.array, width)

    def split(self, sep=None):
        """Divide cada elemento en el array."""
        return np.char.split(self.array, sep)

    def replace(self, old, new):
        """Reemplaza una subcadena en cada elemento del array."""
        return np.char.replace(self.array, old, new)

    def strip(self, chars=None):
        """Elimina los caracteres leading y trailing especificados de cada elemento del array."""
        return np.char.strip(self.array, chars)

    def count(self, sub):
        """Cuenta el número de ocurrencias de una subcadena en cada elemento del array."""
        return np.char.count(self.array, sub)

    def startswith(self, prefix):
        """Devuelve un array de booleanos indicando si cada elemento comienza con el prefijo especificado."""
        return np.char.startswith(self.array, prefix)

    def endswith(self, suffix):
        """Devuelve un array de booleanos indicando si cada elemento termina con el sufijo especificado."""
        return np.char.endswith(self.array, suffix)

    def upper(self):
        """Convierte los caracteres de cada elemento del array a mayúsculas."""
        return np.char.upper(self.array)

    def lower(self):
        """Convierte los caracteres de cada elemento del array a minúsculas."""
        return np.char.lower(self.array)

    def capitalize(self):
        """Capitaliza la primera letra de cada elemento del array."""
        return np.char.capitalize(self.array)