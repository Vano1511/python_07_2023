import pytest
from matrix import Matrix


@pytest.fixture
def matr1():
    return Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])


@pytest.fixture
def matr2():
    return Matrix(Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]]))


@pytest.fixture
def matr3():
    return Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_pair(matr1, matr2):
    assert matr2() != matr1()

