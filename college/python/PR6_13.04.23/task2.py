import tkinter as tk

app = tk.Tk()

onEchoButtonClick = lambda : print("Практична робота №6 виконав студент Групи К 3-1 Сільченко Олексій")

buttonLabel = tk.Label(app,
                       text = 'Натискайте для отримання результату',
                       font = 'Arial'
                       )

echoButton = tk.Button(app,
                       text = 'Надрукувати', 
                       command = onEchoButtonClick,
                       bg = 'green',
                       fg = 'yellow',
                       height = 5,
                       width = 15
                       )
# Упаковка
[v.pack() for _, v in app.children.values()]

app.mainloop()