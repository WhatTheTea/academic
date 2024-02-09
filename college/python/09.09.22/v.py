text = "Уже в дітей порожевіли личка, Уже дощем надихалась рілля. І скрізь трава, Травиченька, Травичка! І сонце сипле квіти, як з бриля!"
newtext = []

deleteFlag = False
for i in range(len(text)):
    s = text[i]
    if (s == "т" or s == "Т") and (text[i-1] == " "):
        deleteFlag = True
    if(s == " "):
        deleteFlag = False
    if deleteFlag:
        s = ""
    newtext.append(s)

print("Result: ", "".join(newtext))
