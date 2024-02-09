import tkinter as tk

app = tk.Tk()

onEchoButtonClick = lambda : print("Практична робота №6 виконав студент Групи К 3-1 Сільченко Олексій")

echoButton = tk.Button(app,
                       text = 'Надрукувати', 
                       command = onEchoButtonClick,
                       bg = 'green',
                       fg = 'yellow'
                       )
# Упаковка
[v.pack() for _,v in app.children.values()]


app.mainloop()