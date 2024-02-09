import tkinter as tk
app = tk.Tk()

# Логіка
checkedRadio = None

# Дизайн
buttonLabel = tk.Label(app,
                       text = 'Натискайте для отримання результату',
                       font = 'Arial 12'
    )

echoButton = tk.Button(app,
                       text = 'Надрукувати', 
                       command = lambda : print("Практична робота №6 виконав студент Групи К 3-1 Сільченко Олексій"),
                       bg = 'green',
                       fg = 'yellow',
                       height = 5,
                       width = 15
    )
firstEntry = tk.Entry(app,
                      width = 10,
                      bd = 2
    )
longText = tk.Text(app,
                   width = 20,
                   font = 'Arial 14',
                   wrap = tk.WORD
    )
radioButtons = [ tk.Radiobutton(app,
                                text = f'{i+1} кнопка',
                                variable = checkedRadio,
                                value = i
                                ) for i in range(3)]
# Упаковка
[v.pack() for _, v in app.children.items()]

app.mainloop()