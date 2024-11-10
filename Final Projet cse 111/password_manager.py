"""
Program: chemistry
Author: Jose Okitandende
Purpose: Writing functions to calculate molar mass of substances
Date: 31/10/2024
"""

# First step is to import all the required module that my program is dependent on
#  ------------------------------------------ MODULES SECTION ---------------------------------- #
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import json
import pyperclip
from random import choice, randint, shuffle

# ---------------------------------------------- CONSTANTS SECTION -------------------------------------- #
CANVAS_BACKGROUND_COLOR = "#0a0c4c"
INPUT_FIELD_COLORS = "#e7e9e2"
TEXT_COLOR = "#f4f7f7"
SEARCH_BUTTON_COLOR = "#5ec7e1"
ADD_BUTTON_COLOR = "#3ece5c"
GENERATE_BUTTON_COLOR = "#e2d4f4"
HIGHLIGHT_COLOR = "#c88e16"
FONT = ("Times New Roman", 14, "normal")

today = datetime.now()
date = f"{today.strftime('%M/%d/%Y | %H:%M:%S')}"


# --------------------------------------------- THE MAIN FUNCTION -------------------------------------- #
def main():
    """This function houses all other functions required for the program to work.
    It also has the get the current date and time."""

    password_gen()
    save_data()
    search_file(web_name)


# -------------------------------------------- PASSWORD SECTION ------------------------------------ #
def password_gen():
    """This function generate a random password from the list of characters and returns a password"""

    characters = ["A", "b", "C", "d", "E", "f", "G", "h", "I", "j", "K", "l", "M", "n", "O", "p", "Q", "r", "S",
                  "t", "U", "v", "W", "x", "Y", "z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "!!", "~", "@", "#", "`", "//",
                  "|", ">", "**", "+", "&", "^", "%", "$", ":", ";", "?", "<<", "(", ")", "{", "]", "''", "_", "--"]
    password_list = [choice(characters) for _ in range(randint(8, 10))]
    shuffle(password_list)
    the_password = "".join(map(str, password_list))
    pyperclip.copy(the_password)
    return pass_code.insert(0, the_password)


# ------------------------------------------- SAVE BUTTON SECTION -------------------------------------- #
def save_data():
    web = web_name.get().upper()
    email = email_name.get()
    password1 = pass_code.get()
    time = date

    if len(web) == 0 or len(email) == 0:
        messagebox.showwarning(title="Empty Field (*required)", message="This input field is empty. Please enter "
                                                                        "the required information")
    elif len(password1) < 8:
        messagebox.showwarning(title="Short Password", message="The length of your password should be 8 "
                                                               "characters or more than.")
    else:
        verification = messagebox.askyesno(title="Confirm", message=f"Are you satisfy with information logged in:\n"
                                                                    f"Website: {web}\nEmail: {email}\nPassword: "
                                                                    f"{password1}")
        if verification:
            the_data = {
                web: {
                    "Email": email,
                    "Password": password1,
                    "Date": time,
                },
            }
            web_name.delete(0, END)
            pass_code.delete(0, END)

            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(the_data, data_file, indent=4)
            else:
                data.update(the_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)


# ----------------------------------------------- SEARCHING THE DATA SECTION ------------------------------------- #
def search_file(name):
    get_name = name.get().upper()
    try:
        with open("data.json", "r") as file:
            data_file = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message="No Data File Found/Such Data File doesn't Exist")
    else:
        if get_name in data_file:
            the_info = data_file[get_name]
            messagebox.showinfo(title=get_name, message=f"Email/Username: {the_info['Email']}\n"
                                                        f"Password: {the_info['Password']}\nDate: {the_info['Date']}")
        else:
            messagebox.showinfo(
                title="Ooops", message=f"Sorry, no details for {get_name} exist in the Data File")


# ----------------------------------------------- GUI SETUP SECTION ------------------------------------- #
window = Tk()
window.title("The Password Manager")
window.config(padx=100, pady=50, background=CANVAS_BACKGROUND_COLOR)
# Establishing the canvas on the window with the background image
canvas = Canvas(width=200, height=200,
                background=CANVAS_BACKGROUND_COLOR, highlightthickness=0)
the_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=the_logo)
canvas.grid(column=1, row=0)
# Establishing the labels and displaying them on the window
website_name = Label(text="Website:", foreground=TEXT_COLOR,
                     background=CANVAS_BACKGROUND_COLOR, font=FONT)
website_name.grid(column=0, row=1)
email_addr = Label(text="Email/Username:", foreground=TEXT_COLOR,
                   background=CANVAS_BACKGROUND_COLOR, font=FONT)
email_addr.grid(column=0, row=2)
password = Label(text="Password:", foreground=TEXT_COLOR,
                 background=CANVAS_BACKGROUND_COLOR, font=FONT)
password.grid(column=0, row=3)
# Establishing the text-fields for the website name, email, and password
web_name = Entry(width=34, borderwidth=1,
                 background=INPUT_FIELD_COLORS, highlightcolor=HIGHLIGHT_COLOR)
web_name.focus()
web_name.grid(column=1, columnspan=2, row=1)
email_name = Entry(width=34, borderwidth=1,
                   background=INPUT_FIELD_COLORS, highlightcolor=HIGHLIGHT_COLOR)
email_name.grid(column=1, columnspan=2, row=2)
pass_code = Entry(width=34, borderwidth=1,
                  background=INPUT_FIELD_COLORS, highlightcolor=HIGHLIGHT_COLOR)
pass_code.grid(column=1, columnspan=2, row=3)
# Establishing the search, generate, and save button on the window
search_btn = Button(text="Search", width=15, command=lambda: search_file(name=web_name),
                    background=SEARCH_BUTTON_COLOR)
search_btn.grid(column=3, row=1)
generate_btn = Button(text="Generate", width=15,
                      command=lambda: password_gen(), background=GENERATE_BUTTON_COLOR)
generate_btn.grid(column=3, row=3)
save_btn = Button(text="Save", width=30, command=save_data,
                  background=ADD_BUTTON_COLOR)
save_btn.grid(column=1, columnspan=2, row=4)

window.mainloop()

if __name__ == '__main__':
    main()