matr_ix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def transpon(matrix):
    """Данная функция принимает матрицу(список списков) и транспонирует ее (столбцы превращает в строки)"""
    new_matrix = []
    for el in list(zip(*matrix)):
        new_matrix.append(list(el))
    return new_matrix


print(transpon(matr_ix))
