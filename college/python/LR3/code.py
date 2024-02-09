import math

try:
    x = int(input("Введіть значення х= "))
    y = int(input("Введіть значення y= "))
    n = int(input("Введіть значення n= "))
except:
    print("Помилка")
    exit()

res = 0
for i in range(1, n+1):
    m = pow(-1, i)*(((x+y)*math.factorial(i))/(math.factorial(i-1)))
    res += m

print("Результат: ", res)