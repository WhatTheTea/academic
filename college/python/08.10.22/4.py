word = input("Слово: ")
symbol = input("Введіть букву: ")
symbolIndex = word.find(symbol)
if symbolIndex >= 0:
    print("Порядковий номер: ", symbolIndex)
else:
    print ("Символ не знайдено!")
