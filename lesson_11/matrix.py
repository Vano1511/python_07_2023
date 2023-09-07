import numpy as np


class Matrix(np.matrix):
    """The Matrix class who inherited from numpy matrix class."""
    def __init__(self, list_of_lists):
        self.matrix = np.matrix(np.array(list_of_lists))

    def __add__(self, other: "Matrix"):
        """The add method with class instances.
            must have matrix with same shapes"""
        if self.matrix.shape == other.matrix.shape:
            return Matrix(self.matrix + other.matrix)
        else:
            return (f"To add we must have matrix with same shapes, "
                    f"but we hawe {self.matrix.shape} and {other.matrix.shape}")

    def __sub__(self, other):
        """The subtract method with class instances.
            must have matrix with same shapes"""
        if self.matrix.shape == other.matrix.shape:
            return Matrix(self.matrix - other.matrix)
        else:
            return (f"To subtract we must have matrix with same shapes, "
                    f"but we have {self.matrix.shape} and {other.matrix.shape}")

    def __mul__(self, other):
        """The multiply method with class instances.
            mustn't have matrix with same shapes"""
        return Matrix(self.matrix * other.matrix)

    def __truediv__(self, other):
        """The divide method with class instances.
            must have matrix with same shapes"""
        if self.matrix.shape == other.matrix.shape:
            return Matrix(self.matrix / other.matrix)
        else:
            return (f"To divide we must have matrix with same shapes, "
                    f"but we have {self.matrix.shape} and {other.matrix.shape}")

    def __str__(self):
        return self.base


if __name__ == "__main__":
    matr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matr2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    print(matr1 / matr2)
