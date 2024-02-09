from tkinter import *
import os

window = Tk()
window.title("Запис до файлу")

name_label = Label(window, text="Введіть інформацію:")
name_label.grid(column=0, row=0)

txt = Text(window,width=30)
txt.grid(column=0, row=1)

def saveToFile():
    filename = "file.txt"
    if not os.path.isfile(filename):
        file = open(filename, "w") # створення файлу
    else: 
        file = open(filename, "a") # додавання інформації до існуючого файлу
        
    info = txt.get('1.0', END)
    file.write(info + "\n")
    file.close()
    message = Label(window, text="Інформація збережена!")
    message.grid(column=0, row=3)
btn = Button(window, text="Зберегти", command=saveToFile)
btn.grid(column=0, row=2)

window.mainloop()