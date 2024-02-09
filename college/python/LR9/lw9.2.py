import tkinter as tk

window = tk.Tk()

def button1Event():
    window.geometry("500x500")
    window["bg"] = "#00FF00"
    window.title("Завдання 2")
window.geometry("150x150")
window["bg"] = "#FFFF00"
button1 = tk.Button(text="Нажми мене", command=button1Event)
button1.pack()
tk.Button(text="Вихід", command=exit).pack()

window.mainloop()