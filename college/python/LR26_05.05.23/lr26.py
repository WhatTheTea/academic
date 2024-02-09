import json
import time
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.simpledialog as simplemb
from dataclasses import dataclass
from typing import List, Tuple

@dataclass(eq=True)
class Question:
    text : str
    answers : List[str]
    answer : str
    isCorrect : bool = False

    def checkAnswer(self, ans : str) -> bool:
        self.isCorrect = self.answer == ans
        return self.isCorrect

def loadQuestions():
    with open('questions.json', 'r') as f:
        for o in json.load(f):
            yield Question(*o.values()) 
    
class App(tk.Tk):
    selectedQuestion : Tuple[int, Question] = (0, None)
    questions = [*loadQuestions()]
    username = ''

    def __init__(self) -> None:
        super().__init__()
        self.geometry('400x300')

        self.username = simplemb.askstring("Тести", "Введіть своє ім'я", parent=self)

        self.info = tk.StringVar(value = 'Для початку натисніть "Вперед"')
        self.infoLabel = ttk.Label(self, 
                                   textvariable=self.info
                                   )
        self.infoLabel.pack()

        self.answersBox = tk.Listbox(self, 
                                     selectmode=tk.MULTIPLE,
                                     )
        self.answersBox.bind("<<ListboxSelect>>", self.onAnswerClick)
        self.answersBox.pack()

        self.answerPanel = ttk.Frame(self)
        self.backButton = ttk.Button(self.answerPanel, 
                                     text = 'Back',
                                     command = self.onBackClick
                                     )
        self.nextButton = ttk.Button(self.answerPanel,
                                     text = 'Next',
                                     command = self.onNextClick
                                     )
        self.res = tk.StringVar(value = 'res')
        self.resLabel = ttk.Label(self.answerPanel,
                                  textvariable = self.res
                                  ) 
        self.answerPanel.pack()
        [v.pack(side=tk.LEFT) for v in list(self.answerPanel.children.values())] 

        self.protocol('WM_DELETE_WINDOW', self.onExit)
        self.changeQuestion(0)
        self.mainloop()
    
    def updateAnswerBox(self, question : Question):
        self.answersBox.delete('0', tk.END)
        [self.answersBox.insert(tk.END,answer) for answer in question.answers]

    def changeQuestion(self, n : int):
        if self.selectedQuestion[0] + n < 0 or self.selectedQuestion[0] + n >= len(self.questions):
            mb.showerror('Помилка', "Більше нема питань")
            return
        self.selectedQuestion = (self.selectedQuestion[0]+n, self.questions[self.selectedQuestion[0]+n])
        self.updateAnswerBox(self.selectedQuestion[1])
        self.info.set(self.selectedQuestion[1].text)
        self.res.set('res')
    
    def onExit(self):
        with open('results.txt', 'a+') as f:
            for q in self.questions:
                s = f'{time.asctime()} | {self.username} | Q: {q.text} is correct: {q.isCorrect}'
                print(s, file=f)
                print()
        self.quit()
    def onBackClick(self):
        self.changeQuestion(-1)

    def onNextClick(self):
        self.changeQuestion(+1)

    def onAnswerClick(self,  e : tk.Event):
        w : tk.Listbox = e.widget
        q = self.selectedQuestion[1]
        self.res.set("yes" if q.checkAnswer(w.selection_get().replace('\n', ',')) else "no")
        
app = App()