import tkinter as tk
app = tk.Tk()

checks = [tk.IntVar(), tk.IntVar()]
checkTexts = ['Перший','Другий']

copyrightLabel = tk.Label(app,
                          text = 'Практична робота №6 виконав студент Групи К 3-1 Сільченко Олексій'
    )
wordListbox = tk.Listbox(app,
                         selectmode = tk.SINGLE,
                         height = 20
    )
checkButtons = [tk.Checkbutton(app,
                               variable = checks[i],
                               text = checkTexts[i]
    ) for i in range(2)]

for s in 'python', 'c++', 'typescript', 'java', 'c#':
    wordListbox.insert(tk.END, s)

[v.pack() for _, v in app.children.items()]

app.mainloop()