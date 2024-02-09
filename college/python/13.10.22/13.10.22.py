friends = ["Alex", "Daria", "Aidos"]
print(friends[0], friends[1], friends[2])

for name in friends:
    print("Привіт,", name)

cars = ["Pagani Zonda Cinque", "Toyota Celica", "Volkswagen Jetta"]
print("Мої улюблені автомобілі: ", end="")
for car in cars:
    print(car, end=", ")
print("\n")