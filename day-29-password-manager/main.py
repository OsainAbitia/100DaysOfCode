from tkinter import *
from tkinter import messagebox
from passwordGenerator import PasswordGenerator

passGen = PasswordGenerator()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_random_password():
    # Clean password input if you press again
    # generate pasword button
    password_input.delete(0, END)
    password_input.insert(0, passGen.random_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        save = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it okay to save?")

        if save:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")
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
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky='ew')
website_input.focus()


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
