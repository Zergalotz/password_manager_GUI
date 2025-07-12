import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master, text, command=None, font=None, bg=None, fg=None, padx=None, pady=None, **kwargs):
        super().__init__(master, text=text, command=command, font=font, bg=bg, fg=fg, padx=padx, pady=pady, **kwargs)

    def set_text(self, text):
        self.config(text=text)