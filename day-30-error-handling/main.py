from tkinter import *
from tkinter import messagebox
from passwordGenerator import PasswordGenerator
import json

passGen = PasswordGenerator()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_random_password():
    # Clean password input if you press again
    # generate pasword button
    password_input.delete(0, END)
    password_input.insert(0, passGen.random_password())

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"{website} not found")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        save = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it okay to save?")

        if save:
            # Manage the existance of our data.json
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Updating old data with new data
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passsword Manager")
window.config(padx=50, pady=50)

# Logo canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


# Website label & input
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=36)
website_input.grid(row=1, column=1)
website_input.focus()

search = Button(text="Search", width=15, command=find_password)
search.grid(row=1, column=2)


# Username label & input
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_input = Entry(width=35)
# Change the insert to autofill te program with your email
username_input.insert(0, "your.email@gmail.com")
username_input.grid(row=2, column=1, columnspan=2, sticky='ew')


# Password label, input & button to generate password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=36)
password_input.grid(row=3, column=1)

generate_password = Button(text="Generate Password",
                           command=create_random_password)
generate_password.grid(row=3, column=2)


# Save website, email & passsword
add_password = Button(text="Add", width=36, command=save)
add_password.grid(row=4, column=1, columnspan=2, sticky='ew')


window.mainloop()
