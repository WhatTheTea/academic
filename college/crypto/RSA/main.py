from Key import Key

class Program:
    _key : Key
    
    def setKeyGenerator(self, key : Key):
        self._key = key
        return self
    
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
                    self._key.createFromTerminal()
                case "2":
                    pass
                case "3":
                    pass
                case _:
                    print("invalid option")
                    exit()

if __name__ == '__main__':
    program = Program().setKeyGenerator(Key("key.pem"))
    program.mainloop()