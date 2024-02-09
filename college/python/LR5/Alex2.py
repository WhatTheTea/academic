def catchException():
    print("error")
    exit()

try: 
    n = int(input("n = "))
except:
    catchException()
if(n < 1 or n > 9):
    catchException()

def getTab(size):
    for i in range(size):
        print(" ", end=" ")
# Верх
for i in range(1, n+1):
    getTab(n-1)
    for j in range(0, n+1):
        if(j > (n - i)):
            print(j, end=" ")
    print()
# Низ
for i in range(0, n):
    getTab(n - (n-i))
    for j in range(n, 0, -1):
        if(j > i):
            print(j, end=" ")
    print()
