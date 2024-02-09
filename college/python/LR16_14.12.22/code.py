def getsubset(st : set, rng : range):
    sub = set()
    i = 0
    for item in st:
        if i < rng.stop:
            sub.add(item)
        i += 1
    return sub

names = {"Вася", "Володя", "Іра"," Ліда", "Марина", "Міша", "Наташа", "Олег", "Оля", "Свєта", "Юля"}
guests = getsubset(names, range(0,5))
group = getsubset(guests, range(1,4))

print(f"Імена: {names}\nГості: {guests}\nПідмножина імен: {guests.issubset(names)}\n" +
f"Група: {group}\nПідмножина імен \ гостей: {group.issubset(names)} \ {group.issubset(guests)}")