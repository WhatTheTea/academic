from random import random
import numpy as np

def findFunc(f, i : list) -> int:
    rowF = [f(r) for r in i]
    return rowF.index(f(rowF))

matrix = [[random() for _ in range(5)] for _ in range(5)]
matrix_T = np.transpose(matrix)
print('Матриця до:\n', matrix)

rowMaxsI = findFunc(max, matrix)
columnMinsI = findFunc(min, matrix_T)

print(np.dot(matrix[rowMaxsI], matrix_T[columnMinsI]))