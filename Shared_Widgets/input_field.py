import tkinter as tk

class CustomInputField(tk.Entry):
    def __init__(self, master, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.default_fg_color = self.cget("fg")
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.set_placeholder()

    def set_placeholder(self):
        if not self.get():
            self.config(fg="grey")
            self.insert(0, self.placeholder)

    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.config(fg=self.default_fg_color)
            self.delete(0, tk.END)

    def on_focus_out(self, event):
        if not self.get():
            self.set_placeholder()