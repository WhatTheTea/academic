from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

if __name__ == '__main__':
    print(
        """МЕНЮ:
        1. Створити ключ
        2. Зашифрувати повідомлення
        3. Розшифрувати повідомлення
        """
    )