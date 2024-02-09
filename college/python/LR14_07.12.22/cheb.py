# Ініціалізація
text = input()
# Ліві дужки заповняються зліва направо, праві - cправа наліво
lefts = [s for s in range(len(text)) if text[s] == "("]
rights = [s for s in range(len(text)-1, -1, -1) if text[s] == ")"]

message = "Зайва {} на позиції {}"
if(len(lefts) + len(rights) > 0):    
    # Видаляються останні елементи списків до спустошення одного з них
    while len(lefts) > 0 and len(rights) > 0:
        lefts.pop()
        rights.pop()
    # Виводяться усі зайві дужки
    if len(lefts) + len(rights) == 0:
        print("Дужок порівно")
    elif len(lefts) < 1:
        [print(message.format(')',i)) for i in rights]
    elif len(rights) < 1:
        [print(message.format('(',i)) for i in lefts]
else:
    print("Дужок немає")