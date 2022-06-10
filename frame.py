import tkinter as tk
from tkinter import ttk

num_wid = 0
def addOne():
    global num_wid
    num_wid += 1
def subOne():
    global num_wid
    num_wid -= 1
def getFrameNum():
    global num_wid
    return num_wid
def add_frame(rootFrame, initCount, initName = "", row = None, col = None):
    if col is None:
        makeFrame(rootFrame, initCount, initName).root.grid()
    else:
        makeFrame(rootFrame, initCount, initName).root.grid(row=row, column=col, padx=10)

    # makeFrame(rootFrame, initCount, initName).root.pack(anchor='w')
    # a = makeFrame(rootFrame, initCount, initName)
    # a.root.pack(anchor='w')
    # a.root.update_idletasks()
    # print(a.root.winfo_width())

class makeFrame:
    def __init__(self, rootFrame, initCount, initName = ""):
        addOne()
        self.root = tk.Frame(rootFrame)
        self.name = tk.Entry(self.root)
        ttk.Button(self.root, text="-", width=3, command=self.deleteFrame).pack(side='left')
        self.name.pack(side='left')
        self.name.insert(tk.END, initName)
        self.label = tk.Label(self.root, text=initCount, width=3, anchor='center')
        self.label.pack(side='left')
        tk.Button(self.root, text="+", repeatdelay=500, repeatinterval=50, command=lambda:self.click_add(1)).pack(side='left')
        tk.Button(self.root, text="-", repeatdelay=500, repeatinterval=50, command=lambda:self.click_add(-1)).pack(side='left')

    def click_add(self, opd):
        num = int(self.label['text'])
        if num+opd >= 0:
            self.label['text'] = num + opd
        self.label.update_idletasks()

    def deleteFrame(self):
        subOne()
        self.root.destroy()