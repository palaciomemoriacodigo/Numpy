import numpy as np

class NumpyIO:
    @staticmethod
    def load(file, mmap_mode=None):
        """
        Carga un array o un objeto guardado en un archivo .npy o .npz.

        Args:
            file (str|file): Ruta del archivo o objeto tipo file desde el cual se va a cargar.
            mmap_mode (str, opcional): Si no es None, se carga el array como memoria mapeada que es guardada en disco.

        Returns:
            array, ndarray, dict: Contenido del archivo .npy o .npz cargado.
        """
        return np.load(file, mmap_mode=mmap_mode)

    @staticmethod
    def save(file, arr):
        """
        Guarda un array en un archivo binario en formato .npy.

        Args:
            file (str|file): Ruta del archivo o objeto tipo file donde se va a guardar el array.
            arr (ndarray): Array de numpy que se va a guardar.
        """
        np.save(file, arr)

    @staticmethod
    def savez(file, *args, **kwds):
        """
        Guarda varios arrays en un archivo único en formato comprimido .npz.

        Args:
            file (str|file): Ruta del archivo o objeto tipo file donde se va a guardar.
            args: Arrays a guardar.
            kwds: Arrays nombrados a guardar.
        """
        np.savez(file, *args, **kwds)

    @staticmethod
    def savetxt(file, arr, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# '):
        """
        Guarda un array en un archivo de texto.

        Args:
            file (str|file): Ruta del archivo o objeto tipo file donde se va a guardar.
            arr (ndarray): Array de numpy que se va a guardar.
            fmt (str|sequence of strs, opcional): Formato de los números en el archivo.
            delimiter (str, opcional): String usado para separar valores.
            newline (str, opcional): String usado para separar líneas nuevas.
            header (str, opcional): String que será escrito al principio del archivo.
            footer (str, opcional): String que será escrito al final del archivo.
            comments (str, opcional): String que será prepuesto a los headers y footers.
        """
        np.savetxt(file, arr, fmt=fmt, delimiter=delimiter, newline=newline, header=header, footer=footer, comments=comments)

    @staticmethod
    def loadtxt(file, dtype=float, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes'):
        """
        Carga datos de un archivo de texto.

        Args:
            file (str|file): Ruta del archivo o objeto tipo file desde el cual se va a cargar.
            dtype (data-type, opcional): Tipo de datos de la matriz resultante.
            comments (str, opcional): El carácter usado para indicar el inicio de un comentario.
            delimiter (str, opcional): El string usado para separar valores.
            converters (dict, opcional): Un diccionario mapeando índices de columna a funciones para convertir esa columna a un tipo de dato.
            skiprows (int, opcional): Salta los primeros 'skiprows' líneas.
            usecols (int|sequence, opcional): Índices de las columnas a leer.
            unpack (bool, opcional): Si True, los arrays resultantes son transpuestos.
            ndmin (int, opcional): Especifica el número mínimo de dimensiones que debe tener el array de salida.
            encoding (str, opcional): Codificación usada para decodificar el texto.
        """
        return np.loadtxt(file, dtype=dtype, comments=comments, delimiter=delimiter, converters=converters, skiprows=skiprows, usecols=usecols, unpack=unpack, ndmin=ndmin, encoding=encoding)
