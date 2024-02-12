from Crypto.PublicKey import RSA

class KeyGenerator:
    def __init__(self, keyPath : str) -> None:
        self.keyPath = keyPath
        
    def createKey(self):
        pwd = input("Введіть пароль для вашого ключа: ")
        self.generateKey(pwd)
        print(f"Ваш ключ успішно записано до {self.keyPath}")

    def generateKey(self, password):
        with open(self.keyPath, "wb") as f:
            key = RSA.generate(3072)
            data = key.export_key(passphrase=password,
                                pkcs=8,
                                protection='PBKDF2WithHMAC-SHA512AndAES256-CBC',
                                prot_params={'iteration_count':131072})
            f.write(data)