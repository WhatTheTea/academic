import random

lst = random.sample(range(-10,10+1),20)

minindex = lst.index(min(lst))
reslst = []
for i in range(0,len(lst)):
    var = lst[i]
    if(i < minindex):
        var*=var
    reslst.append(var)

print("Вхідний масив: ", lst)
print("Вихідний масив: ", reslst)