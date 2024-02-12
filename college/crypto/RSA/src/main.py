from Key import Key
from RSACipher import RSACipher

class Program:
    _key : Key
    _cipher : RSACipher
    textFile = "text.txt"
    
    def setKeyGenerator(self, key : Key):
        self._key = key
        return self

    def setRSACipher(self, rsaCipher : RSACipher):
        self._cipher = rsaCipher
        return self
    
    def setTextFile(self, path : str):
        self.textFile = path
        return self
    
    def encrypt(self):
        with open(self.textFile, "wb") as f:
            message = input("Введіть текст: ")
            self._cipher.loadKey(self._key.publicKeyPath)
            data = self._cipher.encrypt(message)
            f.write(data)
            print("Зашифровано в " + self.textFile)
        
    def decrypt(self):
        with open(self.textFile, "rb") as f:
            message = f.read()
            self._cipher.loadKey(self._key.privateKeyPath)
            data = self._cipher.decrypt(message)
            print("Текст:")
            print(data.decode())
        
    def mainloop(self):
        while True:      
            print("""МЕНЮ:
                    1. Створити ключ""" +
                    ("""
                    2. Зашифрувати повідомлення
                    3. Розшифрувати повідомлення"""
                    if self._key.exists() else ""))
            match(input("Вибір: ")):
                case "1":
                    self._key.generate()
                    print("Пара ключів успішно згенерована")
                case "2":
                    self.encrypt()
                case "3":
                    self.decrypt()
                case _:
                    print("invalid option")
                    exit()

if __name__ == '__main__':
    program = Program().setKeyGenerator(Key()).setRSACipher(RSACipher())
    program.mainloop()