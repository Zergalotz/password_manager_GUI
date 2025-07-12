from tkinter import Label as TkLabel

class Label:
    def __init__(self, master, text):
        self.label = TkLabel(master, text=text)

    def grid(self, **kwargs):
        self.label.grid(**kwargs)

    def config(self, **kwargs):
        self.label.config(**kwargs)