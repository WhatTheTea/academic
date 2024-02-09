
a = int(input("Введіть число: "))

if(a < 0): 
    a = -a

if(a < 10):
    res = "Однозначне"
elif(a < 100):
    res = "Двозначне"
else:
    res = "Багатозначне"

print("Значність: ", res)

if(a % 2 == 0):
    res = "Парне"
else:
    res = "Непарне"

print("Парність: ", res)
