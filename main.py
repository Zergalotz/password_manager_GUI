import random
import pyperclip
from tkinter import *
from tkinter import messagebox
from Constants import constants
from Shared_Widgets import label_widget, button_widget, input_field

""" -------------------------  Password Generator  ------------------------- """
def generate_password():
    random_chars = constants.ALPHABET_CAPS + constants.ALPHABET_LOWER + constants.NUMBERS + constants.SPECIAL_CHARACTERS
    password_length = random.randint(12, 20)
    password = ''.join(random.choice(random_chars) for _ in range(password_length))
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password) # Copy the generated password to clipboard
    website_input.focus()

""" -------------------------    Save Password    -------------------------- """
def add_saved_password():
    # popup message to confirm saving the password
    with open("Saved_Passwords/passwords.txt", "a") as file:
        website = website_input.get()
        email_username = email_username_input.get()
        password = password_input.get()

        if len(email_username) == 0 or len(password) == 0:
            messagebox.showinfo(title="Invalid", message="Please fill in all fields.")
        else:
            is_correct = messagebox.askokcancel(title=website, message=f"Do you want to save the password for {website}?\n"
                                                          f"Email/Username: {email_username}\n"
                                                          f"Password: {password}\n"
                                                          f"Is it correct?")

            if is_correct:
                messagebox.showinfo(title="Info", message="Password saved successfully!")
                if website and email_username and password:
                    file.write(f"{website} | {email_username} | {password}\n")
                    website_input.delete(0, END)
                    email_username_input.delete(0, END)
                    password_input.delete(0, END)
                    website_input.focus()
""" -------------------------       UI Setup      -------------------------- """
# Initialize the main window
window = Tk()
window.title(constants.WINDOW_TITLE)
window.config(padx=constants.WINDOW_PAD_X, pady=constants.WINDOW_PAD_Y)

# Widgets, including labels, buttons, and input fields
canvas = Canvas(width=constants.CANVAS_WIDTH, height=constants.CANVAS_HEIGHT)
logo_image = PhotoImage(file="logo.png")  # Ensure the image file is in the same directory
canvas.create_image(constants.CANVAS_IMAGE_POSITION,image=logo_image)
generate_button = button_widget.CustomButton(window, text="Generate", command=generate_password) #
add_button = button_widget.CustomButton(window, text="Add", command=add_saved_password, width= 27) #
website_label = label_widget.Label(window, text="Website:")
email_username_label = label_widget.Label(window, text="Email/Username:")
password_label = label_widget.Label(window, text="Password:")
website_input = input_field.CustomInputField(window, placeholder="Website URL", width=constants.INPUT_WIDGET_WIDTH)
email_username_input = input_field.CustomInputField(window, placeholder="Email or Username", width=constants.INPUT_WIDGET_WIDTH)
password_input = input_field.CustomInputField(window, placeholder="Password", width=constants.INPUT_PASSWORD_WIDTH)

# Layout the widgets in the window
canvas.grid(row=0, column=1, columnspan=3)
generate_button.grid(row=4, column=3,)
add_button.grid(row=5, column=1, columnspan=3)
website_label.grid(row=2, column=0)
website_input.grid(row=2, column=1, columnspan=3)
website_input.focus()
email_username_label.grid(row=3, column=0)
email_username_input.grid(row=3, column=1, columnspan=3)
email_username_input.focus()
password_label.grid(row=4, column=0)
password_input.grid(row=4, column=1)
password_input.focus()

# Run the main loop to display the window
window.mainloop()