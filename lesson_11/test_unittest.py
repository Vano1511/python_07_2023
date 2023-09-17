import unittest
from matrix import Matrix
from my_exceptions import MatrixShapesError

class MyTestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        self.m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        self.m3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.mult_matr = self.m1 * self.m2
        self.test_mult_matr = Matrix([[30,  24,  18], [84,  69,  54], [138, 114,  90], [192, 159, 126]])

    def test_multiplying(self):
        self.assertTrue(self.mult_matr.all() == self.test_mult_matr.all())
