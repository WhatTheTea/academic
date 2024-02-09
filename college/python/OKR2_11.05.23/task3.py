text = 'Lorem25 ipsum12 dolores22aaaaaaaaaaaaaaaa'
chars = {'a', 'e', 'i', 'o', 'u', 'y'}
print("Голосних" if len(c := [*filter(lambda s : s in chars, text)]) > len(text) - len(c) else "Приголосних та цифр")