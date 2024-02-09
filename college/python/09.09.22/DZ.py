from random import randint
# Variant 12
while True:
    try:
        cols = int(input("columns: "))
        rows = int(input("rows: "))
    except:
        print("Number is not valid")
        continue

    matrix = []

    for i in range(rows):
        tmp = []
        for j in range(cols):
            tmp.append(randint(0,10))
        matrix.append(tmp)

    print("Matrix: ",matrix)

    rowsMaxs = []
    for i in range(len(matrix)):
        elem : list = matrix[i]
        counts = [elem.count(elem[i]) for i in range(len(elem))]
        rowsMaxs.append(max(counts))
    
    maxReps = max(rowsMaxs)
    if(maxReps > 1):
        rowWithMostRepetitions = rowsMaxs.index(maxReps)
        print("Row with most repetitions: ", rowWithMostRepetitions)
    else:
        print("Repetitions were not found")
        
    break 