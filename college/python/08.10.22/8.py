text = input("Введіть символи: ")
newText = ""
for char in text:
    if char.isalpha():
        newText += char
print(newText)
