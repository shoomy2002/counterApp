import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, rootFrame):
        super().__init__(rootFrame)
        self.canvas = tk.Canvas(rootFrame, highlightthickness=0)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollbar_y = ttk.Scrollbar(rootFrame, orient="vertical", command=self.canvas.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        self.canvas.pack(side=tk.LEFT, fill="both", expand=True)
        self.canvas.bind("<MouseWheel>", self.mouse_scroll)

    def mouse_scroll(self, event):
        if event.delta > 0:
            self.canvas.yview_scroll(-1, 'units')
        elif event.delta < 0:
            self.canvas.yview_scroll(1, 'units')