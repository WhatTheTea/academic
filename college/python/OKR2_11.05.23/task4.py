
text = '1 12 123ф1234xx12345 123456t1234567'

counters = []
counter = 0
for s in text:
    if s.isnumeric():
        counter+=1 
    else:
        counters.append(counter)
        counter = 0
counters.append(counter)

print(max(counters))