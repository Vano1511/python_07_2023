import numpy as np
from my_exceptions import MatrixShapesError
import doctest


class Matrix(np.matrix):
    """
    The Matrix class who inherited from numpy matrix class.
    >>> matr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> matr2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    >>> matr1 / matr2
    matrix([[0.11111111, 0.25      , 0.42857143],
            [0.66666667, 1.        , 1.5       ],
            [2.33333333, 4.        , 9.        ]])

    >>> matr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    >>> matr2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    >>> matr1 * matr2
    matrix([[ 30,  24,  18],
            [ 84,  69,  54],
            [138, 114,  90],
            [192, 159, 126]])

    """
    def __init__(self, list_of_lists):
        self.matrix = np.matrix(np.array(list_of_lists))

    def __add__(self, other: "Matrix"):
        """The add method with class instances.
            must have matrix with same shapes"""
        if self.matrix.shape == other.matrix.shape:
            return Matrix(self.matrix + other.matrix)
        else:
            raise MatrixShapesError(self.matrix.shape, other.matrix.shape)

    def __sub__(self, other: "Matrix"):
        """The subtract method with class instances.
            must have matrix with same shapes"""
        if self.matrix.shape == other.matrix.shape:
            return Matrix(self.matrix - other.matrix)
        else:
            raise MatrixShapesError(self.matrix.shape, other.matrix.shape)

    def __mul__(self, other: "Matrix"):
        """The multiply method with class instances.
            mustn't have matrix with same shapes"""
        return Matrix(self.matrix * other.matrix)

    def __truediv__(self, other: "Matrix"):
        """The divide method with class instances.
            must have matrix with same shapes"""
        if self.matrix.shape == other.matrix.shape:
            return Matrix(self.matrix / other.matrix)
        else:
            raise MatrixShapesError(self.matrix.shape, other.matrix.shape)

    def __str__(self):
        return self.base


if __name__ == "__main__":
    doctest.testmod()
    matr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    matr2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    print(matr1 * matr2)
