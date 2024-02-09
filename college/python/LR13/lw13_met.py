#'''  Кортежі '''  створення кортежу
a1 = tuple()
a2 = 1, 2, 3, "abc"
a3 = (1, 2, 3, "abc")
print("Tuple a1 = ", a1)
print("Tuple a2 = ", a2)
print("Tuple a3 = ", a3)
#створення кортежу з інших структур даних
l = [1, 2, 3, "abc"] # зі списку
a4 = tuple(l)
print("Tuple a4 from list l = ", a4)
a5 = tuple("Hello, World!") # з рядка
print("Tuple a5 from string = ", a5)
# вкладеність кортежів
a6 = a2, a3
print("Tuple a6 formed by a2 and a3 = ", a6)
# об'єднання кортежів
a7 = a2 + a3
print("Tuple a7 by combining a2 and a3 = ", a7)
#доступ до елементів кортежів
print("a6[0]: ", a6[0])
print("a6[0][3]: ", a6[0][3])
# a6[0][3] = "cba"
print("\n")
