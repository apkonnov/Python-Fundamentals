import itertools


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        max_len = len(str(max([el for row in self.matrix for el in row]))) + 1
        matrix_str = '\n'.join(' '.join(f'{el: {max_len}d}' for el in line) for line in self.matrix) + '\n'
        return matrix_str

    def __add__(self, other):
        matrix_sum = [[c_1 + c_2 for c_1, c_2 in itertools.zip_longest(r_1, r_2, fillvalue=0)]
                      for r_1, r_2 in itertools.zip_longest(self.matrix, other.matrix,
                                                            fillvalue=[0]*max(len(self.matrix[0]),
                                                                              len(other.matrix[0])))]
        return Matrix(matrix_sum)


matrix_1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
matrix_2 = Matrix([[21, 22, 23, 24], [250, 26, 27, 28], [29, 31, 32, 333]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
