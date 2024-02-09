import tkinter as tk
from tkinter import filedialog as tkfd

app = tk.Tk()

def onButtonClick():
    with open('file2.txt', 'r+') as file:
        lines = list(map(lambda s: s.strip(), file.readlines()))
        textBox.delete('1.0', tk.END)
        text = [*lines, f'Кількість рядків у файлі: {len(lines)}'] 
        textBox.insert(tk.END, text)
        
        file.truncate(0)
        file.seek(0)
        print(*text, file=file, sep='\n')


openButton = tk.Button(app,
                       text = "Відкрити",
                       command = onButtonClick
                       )

textBox = tk.Text(app,
                  font = 'Consolas 10'
                  )

# Упаковка
[v.pack() for _,v in app.children.items()]

app.mainloop()