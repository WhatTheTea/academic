from Key import Key
from RSACipher import RSACipher

class Program:
    _key : Key
    _cipher : RSACipher
    
    def setKeyGenerator(self, key : Key):
        self._key = key
        return self

    def setRSACipher(self, rsaCipher : RSACipher):
        self._cipher = rsaCipher
        return self
    
    def encrypt(self):
        message = input("Введіть текст: ")
        self._cipher.loadKey(self._key.publicKeyPath)
        data = self._cipher.encrypt(message)
        print("Шифротекст:")
        print([a for a in data])
        
    def decrypt(self):
        message = input("Введіть шифротекст: ")
        message = bytes([int(s) for s in message.strip('[]').split(',')])
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