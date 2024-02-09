words = [input("Введіть слово: ") for i in range(5)]
result = []

def palindrome(word: str):
    length = len(word)
    first_half = word[0:(length//2)+1]
    second_half = word[length:(length//2)-1:-1]
    if first_half == second_half:
        return True
    else:
        return False
def char_repeats(word: str):
    for i in range(1, len(word)):
        if(word[i-1] == word[i]): return True
    return False

for w in words:
    if(w == words[0]): continue
    if(not palindrome(w)): continue
    if(char_repeats(w)): continue
    result.append(w)
print(result)
