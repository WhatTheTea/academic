import tkinter as tk
from tkinter import ttk
import random
from typing import List, Tuple

# Умова задачі
def generateInputFile(matrix_size : Tuple[int,int]):
    rows, cols = matrix_size

    def generateMatrix():
        for row in range(rows):
            yield random.sample(range(-cols*rows, cols*rows), cols)

    with open('25V_in.txt', 'w') as file:
        print(*matrix_size, '\n', file = file)
        for row in generateMatrix():
            print(*row, file=file)

# Інтерфейс
class App(tk.Tk):
    FILE_IN = '25V_in.txt'
    FILE_OUT = '25V_out.txt'
    def __init__(self) -> None:
        super().__init__()
        # left
        self.leftFrame = ttk.Frame(self)
        self.inLabel = ttk.Label(self.leftFrame, 
                                 text=self.FILE_IN
                                 )
        self.inText = tk.Text(self.leftFrame,
                              width = 20,
                              height= 20
                              )

        [widget.pack() for _, widget in self.leftFrame.children.items()]
        self.leftFrame.pack(side = tk.LEFT)
        # right
        self.rightFrame = ttk.Frame(self)
        self.outLabel = ttk.Label(self.rightFrame, 
                                  text=self.FILE_OUT
                                  )
        self.outText = tk.Text(self.rightFrame,
                               width = 20,
                               height= 20
                               )
        
        [widget.pack() for _, widget in self.rightFrame.children.items()]
        self.rightFrame.pack(side = tk.RIGHT)

        # top
        self.topFrame = ttk.Frame(self)
        self.rowsLabel = ttk.Label(self.topFrame,
                                   text = 'Рядків:'
                                   )
        self.rowsEntry = ttk.Entry(self.topFrame)
        self.colsLabel = ttk.Label(self.topFrame,
                                   text = 'Стовпців:'
                                   )
        self.colsEntry = ttk.Entry(self.topFrame)
        self.generateInputButton = ttk.Button(self.topFrame,
                                              text = 'Згенерувати вхідний файл',
                                              command = self.onInputButtonClick
                                              )
        self.outputButton = ttk.Button(self.topFrame,
                                       text = 'Виконати програму',
                                       command = self.onOutputButtonClick
                                       )
        [widget.pack() for _, widget in self.topFrame.children.items()]
        self.topFrame.pack(side = tk.TOP)

    def onInputButtonClick(self):
        rows, cols = int(self.rowsEntry.get()), int(self.colsEntry.get())
        generateInputFile((rows,cols))

        with open(self.FILE_IN, 'r') as f:
            for line in f.readlines():
                self.inText.insert(tk.END, line)

    def onOutputButtonClick(self):
        matrix : List[List[int]] = []
        with open(self.FILE_IN, 'r') as f:
            f.seek(6)
            for line in f.readlines():
                matrix.append([int(s) for s in line.split()])
            for row in matrix:
                i_rowmax = row.index(max(row))
                row[0], row[i_rowmax] = row[i_rowmax], row[0]

                self.outText.insert(tk.END, row)
                self.outText.insert(tk.END, '\n')
app = App()
app.mainloop()