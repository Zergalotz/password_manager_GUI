import tkinter as tk
from Constants import constants

class CustomButton(tk.Button):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        self.config(padx=10, pady=5, font=(constants.FONT_TYPE, constants.FONT_SIZE, constants.FONT_STYLE), bg=constants.BACKGROUND_COLOR, fg=constants.FOREGROUND_COLOR)

    def set_text(self, text):
        self.config(text=text)
