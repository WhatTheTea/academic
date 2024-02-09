import numpy as np
def output(event):
    global km, m, sag, rez
    z_km =float(km.get())
    z_m =float(m.get())
    z_sag=float(sag.get())
    # s = s_sag, z_km = x, z_m = a, z_sag = b
    if z_km <= 0:
        raise Exception('км не можуть бути менше 0')
    else:
        s_sag = np.log(z_m) + np.log(z_sag)
        s_sag = round(s_sag, 2)
    print(z_km)
    print(z_m)
    print(z_sag)
    print(s_sag)
    rez.delete(0,END)
    rez.insert(0,s_sag)

from tkinter import *
root = Tk()
root.title('Виразити в саженях значення (…) км + (…) м + (…) сажені')
root['bg'] = 'yellow'
lab = Label(root, text='Виразити в саженях значення (…) км + (…) м + (…) сажені',font='Arial 15',fg='firebrick',bg = 'yellow')
lab.grid(row=0,column=0,padx=20)
lab_km = Label(root, text='Введіть к-ть км',font='Arial 10',bg = 'yellow')
lab_km.grid(row=1,column=0,padx=20)
lab_m = Label(root, text='Введіть к-ть м', font='Arial 10',bg = 'yellow')
lab_m.grid(row=2,column=0,padx=20)
lab_sag = Label(root, text='Введіть к-ть саженів',font='Arial 10',bg = 'yellow')
lab_sag.grid(row=3,column=0,padx=20)
lab_rez1 = Label(root, text='Натисніть на кнопку для розрахунку',font='Arial 10',bg = 'yellow')
lab_rez1.grid(row=4,column=0,padx=20)
lab_rez2 = Label(root, text='Обчислене значення виразу в саженях =',font='Arial 14',bg = 'yellow')
lab_rez2.grid(row=5,column=0,padx=20)
km = Entry(root,width=5,bg='Skyblue1')
m = Entry(root,width=5,bg='Skyblue1')
sag= Entry(root,width=5,bg='Skyblue1')
but = Button(root,text='Виразити в саженях')
rez = Entry(root,width=25,font='Arial 14',bg='salmon2')
km.grid (row=1,column=1,padx=5)
m.grid (row=2,column=1,padx=5)
sag.grid(row=3,column=1,padx=5)
but.grid(row=4,column=1,padx=5)
rez.grid(row=5,column=1,padx=5)
but.bind('<Button-1>',output)
root.mainloop()