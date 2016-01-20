# переписать программу так, чтобы добавление нового поля
# не требовало редактирования более 1 места в этой программе

from tkinter import * #кроссплатформенная библиотека для разработки графического интерфейса

class IntEntry: #строка текста
    def __init__(self, root): #__init__ - конструктор класса; self - параметр метода, работа с различными типами
        self.v = IntVar()
        self.e = Entry(root, textvariable=self.v)
        self.e.pack()
    def getVal(self):
        try:
            return self.v.get()
        except:
            return 0

class StrEntry(IntEntry):
    def __init__(self, root):
        self.v = StringVar()
        self.e = Entry(root, textvariable=self.v)
        self.e.pack()

class EntryStore:
    def __init__(self):
        self.entries = []
    def get(self):
        return self.entries
    def addIntEntry(self, root):
        e = IntEntry(root)
        self.entries.append(e)
    def addStrEntry(self, root):
        e = StrEntry(root)
        self.entries.append(e)

root = Tk() #объект-окно
es = EntryStore()

def f(): # выводит все значения полей
    for v in es.get():
        print(v.getVal())

es.addIntEntry(root)
es.addIntEntry(root)
es.addStrEntry(root)
es.addStrEntry(root)
es.addStrEntry(root)
es.addStrEntry(root)

l = Label(root, text='Your name')
b = Button(root, text='Ok', command=f)

l.pack()
b.pack()

root.mainloop()

