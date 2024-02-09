from dataclasses import dataclass
# Клас даних виробу
@dataclass
class Product:
    _name : str = ''
    _cipher : str = ''
    _count : int = 0
    
    # dataclass автоматично створює __repr__
    def show(self) -> None:
        print(self)

    # Інкапсуляція _name
    def getName(self) -> str:
        return self._name
    def setName(self, name) -> None:
        self._name = name

    # Інкапсуляція _cipher
    def getCipher(self) -> str:
        return self._cipher
    def setCipher(self, cipher) -> None:
        self._cipher = cipher

    # Інкапсуляція _count
    def getCount(self) -> int:
        return self._count
    def setCount(self, count) -> None:
        self._count = count
    #def setCount(self) -> None:
     #   pass
        

a = Product("a","b",3)
print(a.getName())
a.setName("rrrrr")
print(a.getName())
a.show()
b = Product('bbb', 'ccc', 10)
c = Product(*b.__dict__.values())
b.show()
c.show()