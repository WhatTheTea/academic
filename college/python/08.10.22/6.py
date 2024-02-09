string = input("Введіть символи: ")
if string.isdigit():
    print("Тут лише цифри")
elif string.isalpha():
    print("Тут лише букви")
elif string.isalnum():
    print("Тут суміш букв і цифр")
