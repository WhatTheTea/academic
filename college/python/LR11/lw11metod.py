print("ДІАПАЗОНИ")
# [0, 10)
print("")
for i in range(10):
    print('i =', i)
# [5, 10)
print("")
for i in range (5, 10):
    print( 'i =', i)
# [5, 10) крок: 2
print("")
for i in range(5, 10, 2): print('i =', i)
print("")
# Цикл виконається 3 рази, поки користувач не зупине
for i in range(3) :
    response = input('Введіть stop, щоб зупинити цикл ')
    if response == 'stop':
        break
else:
    print( 'Цикл був завершений самостійно')
print('Кінець')
# Зворотній діапазон
print("")
for i in reversed(range(5)) :
    print(i)

print("ЗРІЗИ")
#### Зрізи ####
print("")
my_list = [5, 7, 9, 1, 1, 2]
print(my_list)
pre_last = my_list [-2]
print(pre_last)
result = my_list[0] + my_list[-1];print(result)

print("")
my_list = [5, 7, 9, 1, 1, 2]
print(my_list)

print("")
sub_list = my_list[6:3]
print(sub_list) 

print("")
print(my_list [4:5])
print(my_list[2:-2])

print("")
my_list = [5, 7, 9, 1, 1, 2]
print(my_list)

print("")
sub_list = my_list[0:-1:2]
print(sub_list) 

print("")
print(my_list[2:-2:2])

print("")
print(my_list [-1:0:-1])

print("")
my_list=[5, 7, 9, 1, 1, 2]
print(my_list)
print(my_list [2: ])
print(my_list [ :-2])
print(my_list[ : :-1])
# RANDOM
print("RANDOM")
import random
arr = random.sample(range(-6, 6), 12)
print("our random list: ", arr)
flag = 0

while flag == 0:
    if 0 in arr: 
        first_zero_index = arr. index(0) 
        flag = 1
    else:
        print("we have not at list one zero in list: ")

arr1 = []
if flag == 1:
    for i in arr[first_zero_index: ]:
        arr1.append(i)
print (arr1)