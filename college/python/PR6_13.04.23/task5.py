import tkinter as tk
import tkinter.messagebox as tkmb
app = tk.Tk()

buttonLabel = tk.Label(app,
                       text = "Введіть своє ім'я:",
                       font = 'Arial 13'
                       )
nameEntry = tk.Entry(app,
                     width = 10,
                     bd = 2,
                     )
messageButton = tk.Button(app,
                       text = 'Вивести', 
                       command = lambda : tkmb.showinfo(message = f'Привіт, {nameEntry.get()}')
                       )

# Упаковка
[v.pack() for _, v in app.children.items()]

app.mainloop()