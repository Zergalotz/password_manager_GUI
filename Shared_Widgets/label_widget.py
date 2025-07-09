from tkinter import Label as TkLabel

class Label:
    def __init__(self, master, text):
        self.label = TkLabel(master, text=text)

    def pack(self, **kwargs):
        self.label.pack(**kwargs)

    def config(self, **kwargs):
        self.label.config(**kwargs)