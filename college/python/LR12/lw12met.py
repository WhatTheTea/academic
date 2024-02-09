# Створення матриці
rows = int (input("Введіть число рядків = ") )
columns = int(input("Введіть число стовпців = "))
matrix = []
# Заповнення матриці

for i in range (rows) :
    row = []
    for j in range (columns) :
        elem = int(input("M[{}][{}] = ". format (i, j)))
        row.append(elem)
    matrix.append(row)
# Друк матриці
for i in matrix:
    for j in i:
        print(j, end= " ")
    print()