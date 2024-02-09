import matplotlib.pylab as pl
from matplotlib.animation import FuncAnimation

def countSymbols():
    with open("text.txt", 'r') as f:
        text = f.read()
        # Використання особливості словників зберігати лише 1 копію унікальних ключів
        symbols = {s:0 for s in text if s != '\n' and s != ' '}
        for s in symbols:
            filtered = list(filter(lambda x : x == s, text))
            symbols[s] = len(filtered)
        return symbols
# Сортуємо словник по значенню, перетворюємо кортежі (ключ, значення) назад у словник
symbols = dict(sorted(countSymbols().items(), key = lambda x: x[1], reverse=True))
#                                          # Задаємо усім стовпчикам ширину в 1
# код для миттєвого результату
# pl.bar(symbols.keys(), symbols.values(), [1]*len(symbols))
# pl.savefig(fname = 'fig.png')
fig, ax = pl.subplots()
keys, vals = [],[]
bar = ax.bar(keys,vals)
def update(frame):
    keys.append(frame)
    vals.append(symbols[frame])
    bar = ax.bar(keys,vals, color='black')
    return bar
animation = FuncAnimation(fig, update, frames=list(symbols.keys()))

pl.show()