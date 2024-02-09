import random;

def output(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
# init
matrix = [random.sample(range(-10,11), 3) for i in range(2)]
print("was")    
output(matrix)

i_min_plus = 0
min_plus = 20
i_max_minus = 0
max_minus = -20
# min, max cols
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        element = matrix[i][j]
        if element > 0 and element < min_plus:
            min_plus, i_min_plus = element, j
        if element < 0 and element > max_minus:
            max_minus, i_max_minus = element, j
# swap
for i in range(len(matrix)):
    matrix[i][i_max_minus], matrix[i][i_min_plus] = matrix[i][i_min_plus], matrix[i][i_max_minus]
# output
print("\nnew:")
output(matrix)


