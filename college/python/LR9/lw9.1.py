from tkinter import *

wn=Tk()
def change (event):
    wn.geometry("500x500")
    wn["bg"]="green"
    wn.title("Zavdannya 1")
    Label(wn, text="Сільченко Олексій").place(x= 250, y=250, anchor=CENTER)
wn.bind("<Button-1>", change)
wn.mainloop()