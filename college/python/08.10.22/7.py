text = "4 Christmases Fantastic\n4 The Nutcracker and the\n4 Realms"
newText = ""
for char in text:
    if char == "4":
        char = "Four"
    newText += char
print("Before: ", text)
print("After: ", newText)
