text = "Events happened very rapidly with Francis Morgan that late spring morning"
textLen = len(text)
whitespaceless = len(text.replace(" ", ""))
print(text, "\nКількість слів: ", textLen-whitespaceless+1)
