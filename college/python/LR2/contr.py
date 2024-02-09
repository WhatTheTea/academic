print("Лабораторна робота 2")

try:
    x = float(input("Значення х = "))
    y = float(input("Значення y = "))
except:
    print("Error")
    exit()

if (x >= 2):
    res = x + y + 6
elif (y < 0) and (x < 2):
    res = (y-x)*(-1)
else:
    res = (y+x)/2

print("f = ", res)