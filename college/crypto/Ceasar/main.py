def encode(data : str, offset : int):
    for c in data:
        yield chr(ord(c) + offset)

def decode(data : str, offset : int):
    for c in data:
        yield chr(ord(c) - offset)

readOrWrite = input("1. Розшифрувати\n2. Зашифрувати\n")
offset = int(input("Введіть ключ шифрування: "))
with open("data.txt", "+r") as f:
    data = f.read()

    if readOrWrite == "1":
        data = str().join(decode(data, offset))
    else:
        data = str().join(encode(data,offset))
    
    f.seek(0)
    print(data, file=f)
        