import random

nRows = 5; nCols = 5
matrix = []

for nrow in range(nRows):
    sample = random.sample(range(0,10),5)
    matrix.append(sample)

secondRow = matrix[1]
firstCol = [i[0] for i in matrix]

print("Сума елементів 2 рядка та 1 стовпця: ", sum(secondRow) + sum(firstCol))