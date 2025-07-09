from tkinter import *
from Constants import constants
from Shared_Widgets import label_widget

""" -------------------------  Password Generator  ------------------------- """

""" -------------------------    Save Password    -------------------------- """

""" -------------------------       UI Setup      -------------------------- """
window = Tk()
window.title(constants.WINDOW_TITLE)
window.config(width=constants.WINDOW_WIDTH, height=constants.WINDOW_HEIGHT, padx=constants.PAD_X, pady=constants.PAD_Y)
label = label_widget.Label(window, text="Password Generator")

canvas = Canvas(window, width=constants.CANVAS_WIDTH, height=constants.CANVAS_HEIGHT, bg="white")
logo_image = PhotoImage(file="./Images/logo.png")  # Ensure the image file is in the same directory
canvas.create_image((10 ,10),image=logo_image)
canvas.grid(row=0, column=2, columnspan=3, padx=constants.PAD_X, pady=constants.PAD_Y)

# must be at the end of the file
window.mainloop()