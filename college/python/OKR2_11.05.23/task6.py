from dataclasses import dataclass
from typing import List

@dataclass
class Car:
    manufacturer : str
    model : str
    price : int

@dataclass
class AutoSalon:
    name : str
    cars : List[Car]
    @property
    def CarsPrice(self):
        return sum(map(lambda x : x.price, self.cars))

cars = [Car('AZLK', '2141', 400), Car('Volkswagen', 'Jetta', 600), Car('Daewoo', 'Lanos', 1000)]
autosalon = AutoSalon('LuxAvto', cars)
print(autosalon)
print(autosalon.CarsPrice)