from tkinter import *

# Be careful with types, we get a string from the input
# so we need to convert it to float and then to string
# again


def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# input for miles to calculate
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles = miles_input.get()

# Label for miles
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=50, pady=50)

# Km labels and input
is_iqual_label = Label(text="is iqual to", font=("Arial", 12, "bold"))
is_iqual_label.grid(column=0, row=1)

# Km result label
kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=("Arial", 12, "bold"))
kilometer_label.grid(column=2, row=1)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
