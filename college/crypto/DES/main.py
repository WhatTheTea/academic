from Crypto.Cipher import DES
def textToBlocks(text : str):
    buf = str()
    for i,s in enumerate(text):
        buf+=s
        if (i+1) % 8 == 0 or i == len(text)-1:
            if len(buf) < 8:
                buf = buf + countAndGetSpaces(buf)
            yield buf
            buf = ""
def countAndGetSpaces(iter):
    return (' '* (8 - len(iter)))
def expandBlock(data : bytes): # утворити блок 64 біта при кодуванні utf-8
    return data + countAndGetSpaces(data).encode()
if __name__ == "__main__":
    text = input("Введіть текст: ")
    key = input("Введіть ключ (1-8 символів): ")
    if len(key) > 8: raise Exception("Ключ DES 1-8 байт")
    toBeOrNotToBe = input("МЕНЮ:\n\t1. Шифр \n\t2. Дешифр\nВибір: ")
    # Перетворення рядків на набір байтів
    keyEncoded = expandBlock(key.encode())
    textEncoded = expandBlock(''.join([*textToBlocks(text)]).encode())
    # Створення шифратора
    des = DES.new(keyEncoded, DES.MODE_ECB)

    match toBeOrNotToBe:
        case '1': # шифр
            processed_data= des.encrypt(textEncoded)
            print([*processed_data])
        case '2': # дешифр
            decodedBytes = bytes(int(s) for s in text.strip('[]').split(','))
            processed_data= des.decrypt(decodedBytes)
            print(processed_data.decode())
        case _:
            raise Exception("Incorrect input lmao")
