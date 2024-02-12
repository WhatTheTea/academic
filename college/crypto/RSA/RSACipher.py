from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class RSACipher:
    _key : RSA.RsaKey
    cipher : PKCS1_OAEP.PKCS1OAEP_Cipher
    
    def encrypt(self, message : str):
        return self.cipher.encrypt(message.encode())
    def decrypt(self, message):
        return self.cipher.decrypt(message)
    
    def loadKey(self, path):
        self._key = RSA.importKey(open(path).read())
        self.cipher = PKCS1_OAEP.new(self._key)
    