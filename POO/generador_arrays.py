import numpy as np

# Creamos una clase
class GeneradorArrays:
    # Disponemos el decorador de @staticmethod que permite llamar a los métodos sin necesidad de crear una instancia de la clase 
    # (puedes llamarlos utilizando el nombre de la clase directamente sin necesidad de crear un objeto de esa clase.) 
    #  Nos devuelve una variable que almacena el resultado de llamar al método estático
    @staticmethod
    def zeros(shape, dtype=float):
        """
        Genera un array lleno de ceros con la forma y tipo de datos especificados.
        
        Args:
            shape (tuple): Dimensiones del array.
            dtype (data-type, opcional): Tipo de datos deseado para el array. Por defecto es float.
        
        Returns:
            ndarray: array de ceros con la forma y tipo de datos especificados.
        """
        return np.zeros(shape, dtype=dtype)

    @staticmethod
    def ones(shape, dtype=float):
        """
        Genera un array lleno de unos con la forma y tipo de datos especificados.
        
        Args:
            shape (tuple): Dimensiones del array.
            dtype (data-type, opcional): Tipo de datos deseado para el array. Por defecto es float.
        
        Returns:
            ndarray: array de unos con la forma y tipo de datos especificados.
        """
        return np.ones(shape, dtype=dtype)

    @staticmethod
    def full(shape, fill_value, dtype=None):
        """
        Genera un array lleno con el valor especificado, con la forma y tipo de datos opcionales.
        
        Args:
            shape (tuple): Dimensiones del array.
            fill_value: Valor con el que se llenará el array.
            dtype (data-type, opcional): Tipo de datos deseado para el array.
        
        Returns:
            ndarray: array lleno con el valor especificado y el tipo de datos dado.
        """
        return np.full(shape, fill_value, dtype=dtype)

    @staticmethod
    def arange(start, end, step=1, dtype=float):
        """
        Genera un array con valores en un intervalo especificado.
        
        Args:
            start: Valor inicial del intervalo.
            end: Valor final del intervalo.
            step (int, opcional): Espaciado entre los valores en el intervalo. Por defecto es 1.
            dtype (data-type, opcional): Tipo de datos deseado para el array. Por defecto es float.
        
        Returns:
            ndarray: array que contiene números en un intervalo con el espaciado y tipo de datos especificados.
        """
        return np.arange(start, end, step, dtype=dtype)

    @staticmethod
    def linspace(start, end, num, dtype=float):
        """
        Genera un array de números linealmente espaciados entre los puntos especificados.
        
        Args:
            start: Valor inicial de la secuencia.
            end: Valor final de la secuencia.
            num (int): Número de elementos en la secuencia.
            dtype (data-type, opcional): Tipo de datos deseado para el array. Por defecto es float.
        
        Returns:
            ndarray: array de números linealmente espaciados.
        """
        return np.linspace(start, end, num, dtype=dtype)

    @staticmethod
    def eye(N, M=None, k=0, dtype=float):
        """
        Genera una matriz identidad con las dimensiones y desplazamiento especificados.
        
        Args:
            N (int): Número de filas en la matriz de salida.
            M (int, opcional): Número de columnas en la matriz de salida. Si no se especifica, es igual a N.
            k (int, opcional): Índice de la diagonal. 0 refiere a la diagonal principal, un valor positivo se refiere a una diagonal superior y un negativo a una inferior.
            dtype (data-type, opcional): Tipo de datos de la matriz. Por defecto es float.
        
        Returns:
            ndarray: Matriz identidad con las dimensiones y desplazamiento especificados.
        """
        return np.eye(N, M, k, dtype)

    @staticmethod
    def diag(v, k=0, dtype=float):
        """
        Genera una matriz diagonal basada en el vector dado.
        
        Args:
            v (array): Vector de elementos que formarán la diagonal de la matriz.
            k (int, opcional): Desplazamiento de la diagonal respecto a la principal.
            dtype (data-type, opcional): Tipo de datos de la matriz. Por defecto es float.
        
        Returns:
            ndarray: Matriz con la diagonal especificada.
        """
        return np.diag(v, k).astype(dtype)

    @staticmethod
    def identity(size, dtype=float):
        """
        Genera una matriz identidad de tamaño especificado.
        
        Args:
            size (int): Tamaño de las dimensiones de la matriz (será una matriz cuadrada).
            dtype (data-type, opcional): Tipo de datos de la matriz. Por defecto es float.
        
        Returns:
            ndarray: Matriz identidad de tamaño especificado.
        """
        return np.identity(size, dtype=dtype)
    @staticmethod
    def empty(shape, dtype=float):
        """
        Genera un array sin inicializar con la forma y tipo de datos especificados.
        
        Args:
            shape (tuple): Dimensiones del array.
            dtype (data-type, opcional): Tipo de datos deseado para el array. Por defecto es float.
        
        Returns:
            ndarray: array sin inicializar con la forma y tipo de datos especificados.
        """
        return np.empty(shape, dtype=dtype)

    @staticmethod
    def tri(N, M=None, k=0, dtype=float):
        """
        Genera una matriz triangular inferior con las dimensiones y desplazamiento especificados.
        
        Args:
            N (int): Número de filas en la matriz de salida.
            M (int, opcional): Número de columnas en la matriz de salida. Si no se especifica, es igual a N.
            k (int, opcional): Índice de la diagonal por encima de la cual los elementos son cero. Un valor de k=0 indica la diagonal principal.
            dtype (data-type, opcional): Tipo de datos de la matriz. Por defecto es float.
        
        Returns:
            ndarray: Matriz triangular inferior con las dimensiones y desplazamiento especificados.
        """
        return np.tri(N, M, k, dtype)

    @staticmethod
    def zeros_like(a, dtype=None):
        """
        Genera un array de ceros con la misma forma y tipo de datos que el array dado.
        
        Args:
            a (ndarray): Array que se utiliza como modelo.
            dtype (data-type, opcional): Tipo de datos deseado para el nuevo array. Si es None, se utiliza el tipo de a.
        
        Returns:
            ndarray: Nuevo array de ceros con la misma forma y tipo de datos que a.
        """
        return np.zeros_like(a, dtype=dtype)

    @staticmethod
    def ones_like(a, dtype=None):
        """
        Genera un array de unos con la misma forma y tipo de datos que el array dado.
        
        Args:
            a (ndarray): Array que se utiliza como modelo.
            dtype (data-type, opcional): Tipo de datos deseado para el nuevo array. Si es None, se utiliza el tipo de a.
        
        Returns:
            ndarray: Nuevo array de unos con la misma forma y tipo de datos que a.
        """
        return np.ones_like(a, dtype=dtype)

    @staticmethod
    def full_like(a, fill_value, dtype=None):
        """
        Genera un array lleno con el valor especificado con la misma forma y tipo de datos que el array dado.
        
        Args:
            a (ndarray): Array que se utiliza como modelo.
            fill_value: Valor con el que se llenará el nuevo array.
            dtype (data-type, opcional): Tipo de datos deseado para el nuevo array. Si es None, se utiliza el tipo de a.
        
        Returns:
            ndarray: Nuevo array lleno con el valor especificado con la misma forma y tipo de datos que a.
        """
        return np.full_like(a, fill_value, dtype=dtype)

    @staticmethod
    def copy(a):
        """
        Crea una copia de un array.
        
        Args:
            a (ndarray): Array que se copiará.
        
        Returns:
            ndarray: Una nueva copia del array a.
        """
        return np.copy(a)

    @staticmethod
    def random_rand(*args):
        """
        Genera un array de valores aleatorios con una distribución uniforme entre [0, 1).

        Args:
            *args: Dimensiones del array de salida.

        Returns:
            ndarray: Array de valores aleatorios.
        """
        return np.random.rand(*args)

    @staticmethod
    def random_randint(low, high=None, size=None, dtype=int):
        """
        Genera un array de enteros aleatorios desde `low` (inclusive) hasta `high` (exclusive).

        Args:
            low (int): Valor más bajo de rango (o el más alto si `high` es None).
            high (int, opcional): Valor más alto de rango.
            size (tuple|int, opcional): Dimensiones del array de salida.
            dtype (data-type, opcional): Tipo de datos deseado para el array.

        Returns:
            ndarray: Array de enteros aleatorios.
        """
        return np.random.randint(low, high=high, size=size, dtype=dtype)

    @staticmethod
    def random_randn(*args):
        """
        Genera un array de valores aleatorios con una distribución normal estándar (media = 0, desvío estándar = 1).

        Args:
            *args: Dimensiones del array de salida.

        Returns:
            ndarray: Array de valores aleatorios.
        """
        return np.random.randn(*args)

    @staticmethod
    def random_choice(a, size=None, replace=True, p=None):
        """
        Genera un array aleatorio de muestras de un array dado según las probabilidades especificadas.

        Args:
            a (1-D array-like or int): Si es un array, muestra aleatoriamente de sus elementos. Si es un int, el array es np.arange(a).
            size (int|tuple, opcional): Dimensiones del array de salida.
            replace (bool, opcional): Permitir o no reemplazo.
            p (1-D array-like, opcional): Las probabilidades asociadas con cada entrada en a.

        Returns:
            ndarray: Array de muestras aleatorias.
        """
        return np.random.choice(a, size=size, replace=replace, p=p)

    @staticmethod
    def random_permutation(x):
        """
        Genera una permutación aleatoria de un array.

        Args:
            x (int|array-like): Si es un entero, trata el array como np.arange(x). Si es un array, lo permuta.

        Returns:
            ndarray: Permutación aleatoria del array.
        """
        return np.random.permutation(x)

    @staticmethod
    def random_shuffle(x):
        """
        Modifica un array permutando sus elementos aleatoriamente en el lugar.

        Args:
            x (array-like): El array que será permutado.

        Returns:
            None: Esta función modifica el array en el lugar.
        """
        np.random.shuffle(x)
        return x  # Aunque la función no retorna nada, se devuelve el array modificado para usos en cadena o debugging.