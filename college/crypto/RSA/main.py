from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

KEY_FILE = "key.pem"

def createKey():
    pwd = input("Введіть пароль для вашого ключа: ")
    generateKey(pwd)
    print(f"Ваш ключ успішно записано до {KEY_FILE}")

def generateKey(password):
    with open(KEY_FILE, "wb") as f:
        key = RSA.generate(3072)
        data = key.export_key(passphrase=password,
                              pkcs=8,
                              protection='PBKDF2WithHMAC-SHA512AndAES256-CBC',
                              prot_params={'iteration_count':131072})
        f.write(data)
        
def encryptMessage():
    
    pass

if __name__ == '__main__':
    while True:
        print(
            """МЕНЮ:
            1. Створити ключ
            2. Зашифрувати повідомлення
            3. Розшифрувати повідомлення
            """
        )
        match(input()):
            case "1":
                createKey()
                pass
            case "2":
                pass
            case "3":
                pass
            case _:
                print("invalid option")
                exit()