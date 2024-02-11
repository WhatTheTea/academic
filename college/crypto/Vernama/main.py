import random

def getKeyFor(text : str):
    return str().join([chr(i) for i in random.randbytes(len(text))])
def encode(text : str, key : str):
    for s,k in zip(text,key):
        yield chr(ord(s) ^ ord(k))
def decode(text : str, key : str):
    return encode(text, key)

if __name__ == '__main__':
    data = input("Введіть дані: ")
    choice = input("1. Шифровка\t2. Дешифровка\n")
    if(choice == '1'):
        key = getKeyFor(data)
        encoded = str().join(encode(data, key))
        print(f"Ваш ключ: {key}\nЗашифровані дані: {encoded}")
        with open("key.txt", "w") as f:
            print(encoded, file=f)
            print(key, file=f)
    else:
        key = input("Введіть ключ: ")
        print(str().join(decode(data, key)))