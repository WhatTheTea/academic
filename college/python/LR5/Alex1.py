import math as m

a = 0.25
b = 5
n = 0.3

while a <= b:
    left = a**(5/2) - 0.8
    right = m.log(a**2 + 12.7)
    y = left*right
    print("result:", y, "x =", a)

    a += n