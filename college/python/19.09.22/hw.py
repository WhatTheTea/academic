from random import randint

# Генеруємо файл з буквами та цифрами, 10 рядків
with open("text.txt", 'w') as text:
    for i in range(10):
        print(randint(0,500), chr(randint(0x41,0x5A)), randint(0,500),sep="-",file=text)

# Відкриваємо всі три файли
with open("text.txt") as text, open("cif.txt", "w") as cif, open("lit.txt", "w") as lit:
    for line in text: # перебираємо рядки і символи в них
        stripped = line.strip()
        for char in stripped:
            if char.isalpha(): # відкидаємо букви і цифри в різні файли
                lit.write(char)
            else:
                cif.write(char)
        # додаємо кінець рядку, коли він закінчиться
        lit.write('\n')
        cif.write('\n')