print("Створення розгалуженого процесу")

try:
    x = float(input("Значення х = "))
    y = float(input("Значення y = "))
    z = float(input("Значення z = "))
except:
    print("Error")
    exit()

if (x >= 0):
    f = (x+2) - (y+z)
elif (y != 0) and (z > 0):
    f = 3*(x*x+z)/y
elif (y == 0) and (z > 0):
    f = 3*(x*x*y)/z
else:
    f = (x+y)*z - (x+z)

print("f = ", f)