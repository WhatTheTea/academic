import math

try:
    x = int(input("Введіть значення х= "))
    y = int(input("Введіть значення y= "))
except:
    print("Помилка")
    exit()

res = 0

for i in range(5, 10):
    a = pow(-1, i)
    b = y/x
    c = math.factorial(i+1)/math.factorial(i-1)
    res += a*b*c

print("Результат: ", res)