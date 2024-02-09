def f(x):
    if x >= 5 and x <= 15:
        return (x**2)/(x+1)
    elif x >= 16 and x <= 25:
        return x**3
print("x, f(x)")
for i in range(0, 30 + 1):
    print(i, f(i))