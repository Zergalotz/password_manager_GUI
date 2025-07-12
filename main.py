from tkinter import *
from Constants import constants
from Shared_Widgets import label_widget, button_widget, input_field

""" -------------------------  Password Generator  ------------------------- """
def generate_password():
    # Placeholder for password generation logic
    print("Password generated!")  # Replace with actual password generation logic
""" -------------------------    Save Password    -------------------------- """
def add_saved_password():
    # Placeholder for saving password logic
    print("Password saved!")  # Replace with actual save logic
""" -------------------------       UI Setup      -------------------------- """
window = Tk()
window.title(constants.WINDOW_TITLE)
window.config(padx=constants.WINDOW_PAD_X, pady=constants.WINDOW_PAD_Y)

canvas = Canvas(width=constants.CANVAS_WIDTH, height=constants.CANVAS_HEIGHT)
logo_image = PhotoImage(file="./Images/logo.png")  # Ensure the image file is in the same directory
canvas.create_image(constants.CANVAS_IMAGE_POSITION,image=logo_image)
generate_button = button_widget.CustomButton(window, text="Generate Password", command=generate_password) #
add_button = button_widget.CustomButton(window, text="Add", command=add_saved_password) #
website_label = label_widget.Label(window, text="Website:")
email_username_label = label_widget.Label(window, text="Email/Username:")
password_label = label_widget.Label(window, text="Password:")
website_input = input_field.CustomInputField(window, placeholder="Website URL", width=constants.INPUT_WIDGET_WIDTH)
email_username_input = input_field.CustomInputField(window, placeholder="Email or Username", width=constants.INPUT_WIDGET_WIDTH)
password_input = input_field.CustomInputField(window, placeholder="Password", width=constants.INPUT_WIDGET_WIDTH)

canvas.grid(row=0, column=2, columnspan=3)
generate_button.grid(row=4, column=2, columnspan=3)
add_button.grid(row=5, column=2, columnspan=3)
website_label.grid(row=2, column=1)
website_input.grid(row=2, column=2, columnspan=3)
email_username_label.grid(row=3, column=1)
email_username_input.grid(row=3, column=2, columnspan=3)
password_label.grid(row=4, column=1)
password_input.grid(row=4, column=2, columnspan=3)




# canvas.grid()
# add_button.grid()
# generate_button.grid()


# must be at the end of the file
window.mainloop()