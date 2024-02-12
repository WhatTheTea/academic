import os
from Crypto.PublicKey import RSA

class Key:
    def __init__(self) -> None:
        self.privateKeyPath = "private.pem"
        self.publicKeyPath = "public.pem"
    
    def exists(self):
        return os.path.isfile(self.privateKeyPath)
    
    def generate(self):
        with open(self.publicKeyPath, "wb") as pub, open(self.privateKeyPath, "wb") as pri:
            key = RSA.generate(3072)
            pub.write(key.public_key().export_key())
            pri.write(key.export_key()) # !!! NEEDS PROTECTION IRL !!!