from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

from keyGenerator import KeyGenerator

class Program:
    _keyGenerator : KeyGenerator
    
    def setKeyGenerator(self, kg : KeyGenerator):
        self._keyGenerator = kg
        return self
    
    def mainloop(self):
        while True:      
            print(
                    """МЕНЮ:
                    1. Створити ключ""" +
                    ("""2. Зашифрувати повідомлення
                    3. Розшифрувати повідомлення"""
                    if self._keyGenerator.fileExists() else "")
                    
                    
                )
            match(input()):
                case "1":
                    self._keyGenerator.createKey()
                case "2":
                    pass
                case "3":
                    pass
                case _:
                    print("invalid option")
                    exit()

if __name__ == '__main__':
    program = Program().setKeyGenerator(KeyGenerator("key.pem"))
    program.mainloop()