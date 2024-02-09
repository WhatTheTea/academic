import tkinter as tk
from tkinter import ttk
from typing import List, Tuple

LOREM_IPSUM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas pharetra massa neque, non dapibus eros luctus ac. Nam eu dignissim elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam odio massa, tincidunt sed enim tempus, aliquet tristique lectus. In sollicitudin quam eu libero iaculis semper. Nam elementum mi et lorem viverra tempus. Vivamus nec ornare quam. Duis sit amet nulla leo. Proin malesuada rhoncus lorem, id aliquam ante ultricies nec. Aenean eu quam gravida, varius sem non, scelerisque lorem. Nunc nunc risus, ultrices in venenatis vel, eleifend non magna. Ut ligula dolor, dapibus nec bibendum vel, convallis eu turpis. Nam quis elit vitae orci venenatis posuere nec a nisi. Morbi euismod enim eu molestie lacinia. In nunc ante, vestibulum ut mollis a, mollis nec metus. Ut gravida posuere gravida. """

# Умова задачі
def generateInputFile(matrix_size : Tuple[int,int], r):
    rows, cols = matrix_size
    matrix : List[List[str]] = []
    passed = 0
    for row in range(rows):
        matrix.insert(row, [s for s in LOREM_IPSUM[passed:passed+cols]])
        passed += cols
    
    for col in filter(lambda x: x % 2 != 0,range(cols)):
        cycleColumn(matrix, col, r, 1)
    for row in range(rows):
        cycleRow(matrix, row, row, -1)

    with open('7TASK_in.txt', 'w') as f:
        print(*matrix_size, file = f)
        print(r, '\n', file=f)
        [print(''.join(row), file=f) for row in matrix]
# +1 >>>; -1 <<<
def cycleRow(matrix : List[List[int]], row : int, cycles : int, direction : int) -> List[List[int]]:
    for c in range(cycles):
        moving = matrix[row][0]
        for col in range(0, len(matrix[row]) * direction, direction):
            if col+direction < len(matrix[row]):
                moving, matrix[row][col+direction] = matrix[row][col+direction], moving
            else:
                matrix[row][0] = moving
# +1 VVV; -1 ^^^
def cycleColumn(matrix : List[List[int]], column : int, cycles : int, direction : int) -> List[List[int]]:
    for c in range(cycles):
        moving = matrix[0][column]
        for row in range(0, len(matrix) * direction, direction):
            if row+direction < len(matrix):
                moving, matrix[row+direction][column] = matrix[row+direction][column], moving
            else:
                matrix[0][column] = moving

# Інтерфейс
class App(tk.Tk):
    FILE_IN = '7TASK_in.txt'
    FILE_OUT = '7TASK_out.txt'
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
        self.rLabel = ttk.Label(self.topFrame,
                                   text = 'r:'
                                   )
        self.rEntry = ttk.Entry(self.topFrame)
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
        generateInputFile((rows,cols), int(self.rEntry.get()))

        with open(self.FILE_IN, 'r') as f:
            for line in f.readlines():
                self.inText.insert(tk.END, line)

    def onOutputButtonClick(self):
        matrix : List[List[str]] = []
        with open(self.FILE_IN, 'r') as f:
            f.seek(4)
            r = int(f.read(1))
            f.seek(8)
            for line in f.readlines():
                matrix.append([s for s in line if s != '\n'])
            
            for row in range(len(matrix)):
                cycleRow(matrix, row, row, 1)
            for col in filter(lambda x: x % 2 != 0,range(len(matrix[0]))):
                cycleColumn(matrix, col, r, -1)
            for row in matrix:
                [self.outText.insert(tk.END, col) for col in row]
if __name__ == '__main__':
    app = App()
    app.mainloop()