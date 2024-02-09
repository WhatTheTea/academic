import tkinter as tk

window = tk.Tk()
window.title("Лабораторна робота 9")
window.geometry("500x500")
# events
def paintButtonEvent():
    window["bg"] = "#11CCEE"
    paintLabel.place(anchor= tk.CENTER, x=250, y=150)
    infoLabel["bg"] = window["bg"]

def infoButtonEvent():
    infoLabel.place(anchor=tk.CENTER, x=250, y=200)
# lables
paintLabel = tk.Label(window, 
    text="Це вікно створено\nза допомогою модуля tkinter",
    background="#0000FF",
    font=("Arial", 14))
infoLabel = tk.Label(window,
    text="Сільченко Олексій\nК-3-1",
    font=("Arial", 14))
# buttons
paintButton = tk.Button(window, text="paint", command=paintButtonEvent)
exitButton = tk.Button(window, text="exit", command=exit)
infoButton = tk.Button(window, text="about", command=infoButtonEvent)
# layout
paintButton.place(x=250, y=250, anchor=tk.CENTER)
exitButton.place(x=450, y=450, anchor=tk.CENTER)
infoButton.place(x=250, y=300, anchor=tk.CENTER)

tk.mainloop()