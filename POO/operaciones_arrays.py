import numpy as np

class OperacionesArrays:
    def __init__(self, array):
        """
        Inicializa la instancia con el array proporcionado.

        Args:
            array (ndarray): Array base sobre el que se realizarán las operaciones.
        """
        self.array = array

    def pad(self, pad_width, mode='constant', **kwargs):
        """
        Rellena el array con valores a lo largo de sus bordes.

        Args:
            pad_width (int|tuple): Número de valores añadidos a los bordes de cada eje.
            mode (str, opcional): Modo de relleno, por defecto es 'constant'.
            **kwargs: Argumentos adicionales para modos de relleno específicos.

        Returns:
            ndarray: Array rellenado.
        """
        return np.pad(self.array, pad_width, mode, **kwargs)

    def transpose(self, axes=None):
        """
        Permuta las dimensiones del array.

        Args:
            axes (tuple, opcional): Tupla que contiene la permutación de índices de las dimensiones.

        Returns:
            ndarray: Array transpuesto.
        """
        return np.transpose(self.array, axes)

    def reshape(self, new_shape):
        """
        Da una nueva forma al array sin cambiar sus datos.

        Args:
            new_shape (tuple|int): La nueva forma que debería tener el array.

        Returns:
            ndarray: Array remodelado.
        """
        return np.reshape(self.array, new_shape)

    def resize(self, new_shape):
        """
        Cambia la forma y el tamaño del array, rellenándolo con ceros si aumenta.

        Args:
            new_shape (tuple|int): La nueva forma que debería tener el array.

        Returns:
            ndarray: Array redimensionado.
        """
        resized_array = np.copy(self.array)
        return np.resize(resized_array, new_shape)

    def ravel(self, order='C'):
        """
        Retorna una vista aplanada del array.

        Args:
            order (str, opcional): Orden de los elementos en la vista aplanada ('C' para C-style, 'F' para Fortran-style).

        Returns:
            ndarray: Array aplanado.
        """
        return np.ravel(self.array, order)

    def concatenate(self, other_arrays, axis=0):
        """
        Une una secuencia de arrays junto con el array almacenado a lo largo de un eje existente.

        Args:
            other_arrays (list of ndarray): Arrays que se unirán al array almacenado.
            axis (int, opcional): El eje a lo largo del cual se unen los arrays.

        Returns:
            ndarray: Resultado de la concatenación.
        """
        return np.concatenate([self.array] + other_arrays, axis=axis)

    def vstack(self, other_arrays):
        """
        Apila verticalmente el array almacenado con otros arrays.

        Args:
            other_arrays (list of ndarray): Arrays que se apilarán verticalmente con el array almacenado.

        Returns:
            ndarray: Arrays apilados verticalmente.
        """
        return np.vstack([self.array] + other_arrays)

    def hstack(self, other_arrays):
        """
        Apila horizontalmente el array almacenado con otros arrays.

        Args:
            other_arrays (list of ndarray): Arrays que se apilarán horizontalmente con el array almacenado.

        Returns:
            ndarray: Arrays apilados horizontalmente.
        """
        return np.hstack([self.array] + other_arrays)

    def split(self, indices_or_sections, axis=0):
        """
        Divide el array almacenado en múltiples sub-arrays.

        Args:
            indices_or_sections (int|array-like): Si es un entero, el número de partes iguales para dividir el array. Si es un array, los índices en los que dividir.
            axis (int, opcional): Eje a lo largo del cual dividir.

        Returns:
            list of ndarray: Lista de sub-arrays.
        """
        return np.split(self.array, indices_or_sections, axis=axis)

    def column_stack(self, other_arrays):
        """
        Apila columnas del array almacenado con otros arrays.

        Args:
            other_arrays (list of ndarray): Arrays que se apilarán como columnas con el array almacenado.

        Returns:
            ndarray: Arrays apilados como columnas.
        """
        return np.column_stack([self.array] + other_arrays)

    def tile(self, reps):
        """
        Construye un array por repetición del array almacenado.

        Args:
            reps (int|array-like): El número de repeticiones del array en cada eje.

        Returns:
            ndarray: Array repetido.
        """
        return np.tile(self.array, reps)

    def repeat(self, repeats, axis=None):
        """
        Repite los elementos del array almacenado.

        Args:
            repeats (int|array-like): Número de veces que se repetirá cada elemento.
            axis (int, opcional): Eje a lo largo del cual repetir.

        Returns:
            ndarray: Array con elementos repetidos.
        """
        return np.repeat(self.array, repeats, axis=axis)

    def sum(self, axis=None):
        """Calcula la suma de los elementos del array."""
        return np.sum(self.array, axis=axis)

    def prod(self, axis=None):
        """Calcula el producto de los elementos del array."""
        return np.prod(self.array, axis=axis)

    def mean(self, axis=None):
        """Calcula la media aritmética de los elementos del array."""
        return np.mean(self.array, axis=axis)

    def std(self, axis=None, ddof=0):
        """Calcula la desviación estándar de los elementos del array."""
        return np.std(self.array, axis=axis, ddof=ddof)

    def var(self, axis=None, ddof=0):
        """Calcula la varianza de los elementos del array."""
        return np.var(self.array, axis=axis, ddof=ddof)

    def median(self, axis=None):
        """Calcula la mediana de los elementos del array."""
        return np.median(self.array, axis=axis)

    def percentile(self, q, axis=None):
        """Calcula el percentil q-ésimo de los elementos del array."""
        return np.percentile(self.array, q, axis=axis)

    def quantile(self, q, axis=None):
        """Calcula el cuantil q-ésimo de los elementos del array."""
        return np.quantile(self.array, q, axis=axis)

    def min(self, axis=None):
        """Encuentra el valor mínimo de los elementos del array."""
        return np.min(self.array, axis=axis)

    def max(self, axis=None):
        """Encuentra el valor máximo de los elementos del array."""
        return np.max(self.array, axis=axis)

    def cumsum(self, axis=None):
        """Calcula la suma acumulativa de los elementos del array."""
        return np.cumsum(self.array, axis=axis)

    def cumprod(self, axis=None):
        """Calcula el producto acumulativo de los elementos del array."""
        return np.cumprod(self.array, axis=axis)

    def corrcoef(self):
        """Calcula el coeficiente de correlación de Pearson de los elementos del array."""
        return np.corrcoef(self.array)

    def any(self, axis=None):
        """Comprueba si algún elemento del array es True."""
        return np.any(self.array, axis=axis)

    def all(self, axis=None):
        """Comprueba si todos los elementos del array son True."""
        return np.all(self.array, axis=axis)

    def less(self, other):
            """Compara dos arrays elemento a elemento (menor que)."""
            return np.less(self.array, other)

    def less_equal(self, other):
        """Compara dos arrays elemento a elemento (menor o igual que)."""
        return np.less_equal(self.array, other)

    def greater(self, other):
        """Compara dos arrays elemento a elemento (mayor que)."""
        return np.greater(self.array, other)

    def greater_equal(self, other):
        """Compara dos arrays elemento a elemento (mayor o igual que)."""
        return np.greater_equal(self.array, other)

    def equal(self, other):
        """Compara dos arrays elemento a elemento (igual)."""
        return np.equal(self.array, other)

    def not_equal(self, other):
        """Compara dos arrays elemento a elemento (no igual)."""
        return np.not_equal(self.array, other)

    def argmin(self):
        """Devuelve los índices de los mínimos elementos a lo largo de un eje."""
        return np.argmin(self.array)

    def argmax(self):
        """Devuelve los índices de los máximos elementos a lo largo de un eje."""
        return np.argmax(self.array)

    def argsort(self):
        """Devuelve los índices que ordenarían un array."""
        return np.argsort(self.array)

    def where(self, condition, x, y):
        """Devuelve elementos elegidos de `x` o `y` dependiendo de `condition`."""
        return np.where(condition, x, y)

    def extract(self, condition):
        """Devuelve los elementos del array que cumplen con la condición."""
        return np.extract(condition, self.array)
    
    def isnan(self):
        """Comprueba si los elementos del array son NaN."""
        return np.isnan(self.array)

    def isinf(self):
        """Comprueba si los elementos del array son infinitos."""
        return np.isinf(self.array)

    def isfinite(self):
        """Comprueba si los elementos del array son finitos."""
        return np.isfinite(self.array)

    def nan_to_num(self, copy=True):
        """
        Reemplaza NaN con cero y infinito con números grandes finitos.
        
        Args:
            copy (bool, opcional): Si se debe retornar una copia o modificar el array in-place.
        
        Returns:
            ndarray: Array modificado.
        """
        return np.nan_to_num(self.array, copy=copy)

    def nanmean(self):
        """Calcula la media del array, ignorando los NaN."""
        return np.nanmean(self.array)

    def nanvar(self):
        """Calcula la varianza del array, ignorando los NaN."""
        return np.nanvar(self.array)

    def nanstd(self):
        """Calcula la desviación estándar del array, ignorando los NaN."""
        return np.nanstd(self.array)

    def allclose(self, other, rtol=1e-05, atol=1e-08):
        """
        Comprueba si todos los elementos de dos arrays son iguales dentro de una tolerancia.
        
        Args:
            other (ndarray): Otro array para comparar.
            rtol (float, opcional): Tolerancia relativa.
            atol (float, opcional): Tolerancia absoluta.
        
        Returns:
            bool: True si todos los elementos son iguales dentro de la tolerancia.
        """
        return np.allclose(self.array, other, rtol=rtol, atol=atol)

    def isclose(self, other, rtol=1e-05, atol=1e-08):
        """
        Comprueba elemento por elemento si son iguales dentro de una tolerancia.
        
        Args:
            other (ndarray): Otro array para comparar.
            rtol (float, opcional): Tolerancia relativa.
            atol (float, opcional): Tolerancia absoluta.
        
        Returns:
            ndarray: Array de valores booleanos.
        """
        return np.isclose(self.array, other, rtol=rtol, atol=atol)

    def interp(self, xp, fp, x):
        """
        Realiza una interpolación lineal en un array 1D.
        
        Args:
            xp (1D array): Los valores x en los puntos de datos.
            fp (1D array): Los valores y en los puntos de datos.
            x (ndarray|scalar): Los valores x para los cuales interpolar.
        
        Returns:
            ndarray|scalar: Los valores y interpolados.
        """
        return np.interp(x, xp, fp)