text = "By Red Flower Bagheera meant fire, only no creature in the jungle will call fire by its proper name."
upper = 0; lower = 0; space = 0
for i in text:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1
    if i == " ":
        space += 1
print("Ups: ", upper, "\nLows: ", lower, "\nSpaces: ", space)
