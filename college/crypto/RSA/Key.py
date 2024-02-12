import os
from Crypto.PublicKey import RSA

class Key:
    def __init__(self, keyPath : str) -> None:
        self.keyPath = keyPath
    
    def exists(self):
        return os.path.isfile(self.keyPath)
    

    def generate(self, password):
        with open(self.keyPath, "wb") as f:
            key = RSA.generate(3072)
            data = key.export_key(passphrase=password,
                                pkcs=8,
                                protection='PBKDF2WithHMAC-SHA512AndAES256-CBC',
                                prot_params={'iteration_count':131072})
            f.write(data)
    
    def createFromTerminal(self):
        pwd = input("Введіть пароль для вашого ключа: ")
        self.generate(pwd)
        print(f"Ваш ключ успішно записано до {self.keyPath}")