word1=input('Введіть перше слово: ')
word2=input('Введіть друге слово: ')
result = []

if word1>word2:
    bigger, lesser = word1, word2
else:
    bigger, lesser = word2, word1
for i in range(len(bigger)):
    if i <= len(lesser)-1:
        if bigger[i] != lesser[i]:
            result.append(bigger[i]+lesser[i])
    else:
        result.append(bigger[i])
print(result)