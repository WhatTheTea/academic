from dataclasses import dataclass
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
import json
from typing import List

N_ANSWERS = 5

@dataclass(eq=True, frozen=True)
class Question:
    text : str
    answers : List[str]
    answer : str
    
class App(tk.Tk):
    savedQuestions : List[dict] = []
    savePath : str = None
    def __init__(self) -> None:
        super().__init__()
        self.geometry('400x300')

        self.text = tk.StringVar(self,"Текст питання")
        self.answerChecks = [tk.BooleanVar(self, False) for _ in range(N_ANSWERS)]
        self.answers = [tk.StringVar(self, '') for _ in range(N_ANSWERS)]

        self.textEntry = ttk.Entry(self, textvariable=self.text)
        self.textEntry.pack(pady=(0,10))
 
        self.answersPanel = ttk.Frame(self)
        self.answerCheckbuttons = [ttk.Checkbutton(self.answersPanel, variable=self.answerChecks[i]) for i in range(N_ANSWERS)]
        [self.answerCheckbuttons[i].grid(column=0, row=i, pady=8) for i in range(N_ANSWERS)]

        self.answerEntries = [ttk.Entry(self.answersPanel, textvariable=self.answers[i]) for i in range(N_ANSWERS)]
        [self.answerEntries[i].grid(column=1, row=i) for i in range(N_ANSWERS)]
        self.answersPanel.pack()

        self.saveButton = ttk.Button(self, 
                                     text='Зберегти',
                                     command=self.onSaveButtonClick)
        self.saveButton.pack()

        self.mainloop()
    
    def onSaveButtonClick(self):
        self.savePath = tkfd.asksaveasfilename(defaultextension='.json', parent=self) if not self.savePath else self.savePath
        self.saveFile(self.savePath)
        self.text.set('')
        [a.set(False) for a in self.answerChecks]
        [s.set('') for s in self.answers]

    def saveFile(self, path : str):
        qText = self.text.get()
        qAnswers = list(map(lambda x : x.get(), self.answers))
        qTrueAnswers = ''
        for i in range(N_ANSWERS):
            if self.answerChecks[i].get():
                if i > 1:
                    qTrueAnswers += ","
                qTrueAnswers += self.answerEntries[i].get() 
        q = Question(qText, qAnswers, qTrueAnswers)
        self.savedQuestions.append(q.__dict__)
        with open(path, 'w') as file:
            json.dump(self.savedQuestions, file)

a = App()