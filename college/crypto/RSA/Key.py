import os
from Crypto.PublicKey import RSA

class Key:
    def __init__(self, keyPath : str) -> None:
        self.keyPath = keyPath
    
    def exists(self):
        return os.path.isfile(self.keyPath)
    

    def generate(self):
        with open(self.keyPath, "wb") as f:
            key = RSA.generate(3072)
            data = key.public_key().export_key()
            f.write(data)
    
    def createFromTerminal(self):
        # pwd = input("Введіть пароль для вашого ключа: ")
        self.generate()
        print(f"Ваш ключ успішно записано до {self.keyPath}")